import pandas as pd


class DataCleaning:
    
    def __init__(self):
        pass

    def clean_user_data(self, df):
        '''This method cleans the user data to make sure there are no anomilies within the table.
        
        Args:
            df(dataframe): Takes the pandas dataframe as the parameter.

        Return:
            Returns the legacy users cleaned with no anomilies.
        '''
        df = df.replace(['null', 'NULL', 'NaN', 'None'], pd.NA)
        df = df.dropna(inplace= True)
        df['join_date'] = pd.to_datetime(df['join_date'], errors= 'coerce')
        df['join_date'] = df['join_date'].fillna(pd.Timestamp('1000-01-01'))