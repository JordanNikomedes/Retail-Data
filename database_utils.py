import yaml
import psycopg2
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import inspect



class DatabaseConnector:

    def __init__(self):
        pass

    def read_db_creds(self, name):
        """This method opens the yaml file safely and reads it as a dictionary when called.

        Args:
            name(str): passes the file name as a parameter.

        Returns:
            A dictionary of the yaml file into the terminal.

        Raises:
            raises an error into the console when the content is not valid or has difficulty loading it.
        """

        with open(name, 'r') as file:

            try:
                return yaml.safe_load(file)
            except yaml.YAMLError as exc:
                print(exc)

    def init_db_engine(self, cred):
        """This method estabilishes the connection between the database and the local 
        interface using the sqlalchemy library to create the engine.
        
        Args:
            cred(str): Using the returned output of the read_db_creds method to then parsing
            it through to the engine.

        Return:
            Returns an established connection to the database to then manipulate said data. 
        """

        engine = create_engine(
            f"{'postgresql'}+{'psycopg2'}://{cred['RDS_USER']}"
            f":{cred['RDS_PASSWORD']}@{cred['RDS_HOST']}"
            f":{cred['RDS_PORT']}/{cred['RDS_DATABASE']}"
        )
        return engine
    
    def list_db_table(self, engine):
        """This method lists the tables in the database using the inspect method from the
        sqlalchemy library.
        
        Args:
            engine(obj): Uses the engine from the init_db_engine method to retrieve the tables.
        
        Return:
            Returns the tables from the database and lists them into the console.
        """

        inspector = inspect(engine)
        return inspector.get_table_names()

    def upload_to_db(self,df,name,engine):
        '''This method converts the dataframe back to its original state, uploading it back to the database
        
        Args:
            df(dataframe): takes the pandas dataframe as a parameter.
            name(dataframe): name of the targeted table.
            engine(obj): connecting to the database.

        Return:
            Returns the dataframe back to its original state.
        '''
        df.to_sql(name, engine, if_exists='replace')





if __name__ == '__main__':
    db = DatabaseConnector()
    cred = db.read_db_creds("db_creds.yaml") 
    engine = db.init_db_engine(cred)
    engine.connect()
    print("Hello") 
    print(engine)
    tables_list = db.list_db_table(engine)
    print(tables_list)
    with engine.begin() as conn:
        table = pd.read_sql_table(tables_list[2], con=conn)
    print(table)
