import yaml
import psycopg2
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







#if __name__ == '__main__':

    #data = DatabaseConnector('db_creds.yaml')

    #print(data.read_db_creds())