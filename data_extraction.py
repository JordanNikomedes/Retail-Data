import pandas as pd

class DataExtractor:

    def __init__(self):
        pass

    def read_rds_table(self, engine, table_name):

        with engine.begin() as conn:
            return pd.read_sql_table(table_name, con=conn)

        

    
    









#if __name__ == '__main__':

    #jordan = DataExtractor()
    #query = 'SELECT * FROM table'

    #print(jordan.read_data(query))
