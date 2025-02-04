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


if __name__ == '__main__':

    dim_users()