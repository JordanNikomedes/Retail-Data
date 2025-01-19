class DataCleaning:
    
    def __init__(self):
        pass

    def clean_user_data(self, df):
        df = self.clean_invalid_date(df)