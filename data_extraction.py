import pandas as pd
import tabula
import json
import requests
import boto3
import botocore
from botocore import UNSIGNED
from botocore.config import Config

class DataExtractor:

    def __init__(self):
        pass

    def read_rds_table(self, engine, table_name):
        """This method reads the table from the database, 
        then converts it into a pandas dataframe so it can be manipulated easier within python.
        
        Args:
            engine(obj): parses the engine to connect with the database.
            table_name(str): converts the targeted table into a dataframe.
        
        Return:
            Returns a dataframe using the pandas library.
        """

        with engine.begin() as conn:
            return pd.read_sql_table(table_name, con=conn)
        
    def retrieve_pdf_data(self, link):
        return pd.concat(tabula.read_pdf(link, pages='all'))
    
    def API_key(self):
        return {'x-api-key':'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'}
    
    def list_number_of_stores(self):
        '''This method retrieves the data from the api and puts it into a json format'''
        api_url_base = 'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores'
        response = requests.get(
                                api_url_base,
                                headers=self.API_key()
                                )
        return response.json()['number_stores']

    def retrieve_stores_data(self):
        '''This method retrieves the data from the bucket and puts it into a json format. Then converts
        into pandas dataframe'''
        list_of_frames = []
        store_number = self.list_number_of_stores()
        for _ in range(store_number):
            api_url_base = f'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{_}'
            response = requests.get(
                                    api_url_base,
                                    headers=self.API_key()
                                    )
            list_of_frames.append( pd.json_normalize(response.json()))
        return pd.concat(list_of_frames)
    
    def extract_from_s3(self):
        '''This method reaches the data from aws s3 bucket giving status codes if it was successful'''
        s3 = boto3.client("s3", config=Config(signature_version=UNSIGNED))
        response = s3.get_object(Bucket='data-handling-public', Key='products.csv')
        status   = response.get("ResponseMetadata", {}).get("HTTPStatusCode")
        if status == 200:
            print(f"Successful S3 get_object response. Status - {status}")
            return pd.read_csv(response.get("Body"))
        else:
            print(f"Unsuccessful S3 get_object response. Status - {status}")

    def extract_s3_with_link(self):
        '''This method retieves data from json file in s3 bucket and converts to a
        pandas dataframe'''
        url = 'https://data-handling-public.s3.eu-west-1.amazonaws.com/date_details.json'
        response = requests.get(url) 
        dic = response.json()
        df = pd.DataFrame([])
        for column_name in dic.keys():
            value_list = []
            for _ in dic[column_name].keys():
                value_list.append(dic[column_name][_])
            df[column_name] = value_list
        return df
        

        

    
    










