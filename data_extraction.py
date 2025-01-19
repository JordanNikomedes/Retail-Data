import pandas as pd

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

        

    
    










