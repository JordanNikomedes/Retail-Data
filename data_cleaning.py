import pandas as pd


class DataCleaning:
    
    def __init__(self):
        pass

    def clean_user_data(self, df):
        df = df.replace(['null', 'NULL', 'NaN', 'None'], pd.NA)
        df = df.dropna(inplace= True)
        df['join_date'] = pd.to_datetime(df['join_date'], errors= 'coerce')
        df['join_date'] = df['join_date'].fillna(pd.Timestamp('1000-01-01'))