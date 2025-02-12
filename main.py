import pandas as pd
from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning


def dim_users():
    du = DatabaseConnector()
    de = DataExtractor()
    dc = DataCleaning()

    #connecting the engine and listing dataframe
    cred = du.read_db_creds('db_creds.yaml')
    engine = du.init_db_engine(cred)
    engine.connect()
    tables_list = du.list_db_table(engine)

    #cleaning dataframe
    df_name = tables_list[2]
    df = dc.clean_user_data(de.read_rds_table( engine, df_name))
    print(df.head())

    #uploading to local database
    cred2 = du.read_db_creds('db_creds_local.yaml')
    engine2 = du.init_db_engine(cred2)
    engine2.connect()
    du.upload_to_db(df, 'dim_users', engine2)

def dim_card_details():
    du = DatabaseConnector()
    de = DataExtractor()
    dc = DataCleaning()

    # convert pdf to dataframe
    table = de.retrieve_pdf_data('https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf')
    print(table.head())
    # cleaning the card details
    table = dc.clean_card_data(table)

    # uploading data to local host
    cred = du.read_db_creds('db_creds_local.yaml')
    engine = du.init_db_engine(cred)
    engine.connect()
    du.upload_to_db(table, 'dim_card_details', engine)

def dim_store_details():
    du = DatabaseConnector()
    de = DataExtractor()
    dc = DataCleaning()  
    # retrieving the data
    table = de.retrieve_stores_data()
    print(table[table['store_code']=='WEB-1388012W'])
    table.to_csv('dim_store_details.csv')
    # cleaning the data
    table = dc.called_clean_store_data(table)
    # uploading data to local host
    cred = du.read_db_creds("db_creds_local.yaml") 
    engine = du.init_db_engine(cred)
    engine.connect()
    du.upload_to_db(table, 'dim_store_details', engine)


if __name__ == '__main__':

    #dim_users()
    #dim_card_details()
    dim_store_details()

