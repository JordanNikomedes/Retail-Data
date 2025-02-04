import pandas as pd
import re
import numpy as np

class DataCleaning:
    
    def __init__(self):
        pass

    def remove_null(self, d_table):

        # Removes all null values within the table

        self.d_table = pd.DataFrame(d_table)
        self.d_table.replace(['null', 'None', 'NA'], pd.NA)
        self.d_table.dropna(inplace=True)
        return self.d_table
    
    def valid_date(self, table, date_column):

        # Converts all dates into the correct format

        table[date_column] = pd.to_datetime(table[date_column], errors= 'coerce')
        return table[date_column]

    def valid_email(self, table, mail_column):

        # Makes sure the email is in the correct format

        for i, email in enumerate(table[mail_column]):
            pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

            if not re.match(pattern, email):
                table.loc[i, mail_column] = np.nan
        
        table.dropna(subset=[mail_column], inplace= True)
        return table[mail_column]
    
    def valid_phone_no(self, table, phone_column):

        # Makes sure phone number in the correct format

        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        for i, phone in enumerate(table[phone_column]):
            if not re.match(pattern, phone):
                table.loc[i, phone_column] = np.nan

        table.dropna(subset= [phone_column], inplace= True)
        return table[phone_column]
    
    
    
    
    
    
    
    def clean_user_data(self, table):
        '''This method cleans the user data to make sure there are no anomilies within the table.
        
        Args:
            table(dataframe): Takes the pandas dataframe as the parameter.

        Return:
            Returns the legacy users cleaned with no anomilies.
        '''

        self.remove_null(table)
        self.valid_date(table, 'date_of_birth')
        self.valid_date(table, 'join_date')
        self.valid_email(table, 'email_address')
        self.valid_phone_no(table, 'phone_number')

        #print(table)
        return table
