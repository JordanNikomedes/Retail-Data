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
    
    def check_math_operation(self,value):
        if 'x' in value:
            value.replace(' ','')
            lis_factors = value.split('x')
            return str(float(lis_factors[0])*float(lis_factors[1]))
        return value
    
    def isDigits(self,num):
        '''This method checks if output is integer'''
        return str(num) if str(num).isdigit() else np.nan
    
    def isfloat(self,num):
        '''This method checks if integer is a float'''
        try:
            float(num)
            return True
        except ValueError:
            return False
    
    def get_grams(self,value):
        '''This method holds an if statement to check and replace the units inot grams and kilograms'''
        value = str(value)
        value = value.replace(' .','')
        if value.endswith('kg'):
            value = value.replace('kg','')
            value = self.check_math_operation(value)
            return 1000*float(value) if self.isfloat(value) else np.nan
        elif value.endswith('g'):   
            value = value.replace('g','')
            value = self.check_math_operation(value)
            return float(value) if self.isfloat(value) else np.nan
        elif value.endswith('ml'):   
            value = value.replace('ml','')
            value = self.check_math_operation(value)
            return float(value) if self.isfloat(value) else np.nan
        elif value.endswith('l'):   
            value = value.replace('l','')
            value = self.check_math_operation(value)
            return 1000*float(value) if self.isfloat(value) else np.nan
        elif value.endswith('oz'):   
            value = value.replace('oz','')
            value = self.check_math_operation(value)
            return 28.3495*float(value) if self.isfloat(value) else np.nan
        else:
            np.nan
    
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

    def clean_card_data(self, table):
        '''This method removes any nomalies inside the data in the PDF file'''
        self.valid_date(table, 'date_payment_confirmed')
        self.remove_null(table)

        try:
            assert table['card_number'].str.isdigit()
        except:
            AssertionError

        return table
    
    def called_clean_store_data(self, table):
        '''This method cleans the data from the data from the API'''
        table.drop(columns='lat',inplace=True)
        table = self.valid_date(table,'opening_date')
        table = self.remove_null(table)

        return table
    
    def convert_product_weights(self, table, column_name):
        '''This method converts the weights inside the data to a consistent unit of measurement'''
        table[column_name] = table[column_name].apply(self.get_grams)
        return table
    
    def clean_products_data(self, table):
        '''This method cleans the table of any anomalies and null values'''
        table = self.valid_date(table,'date_added')
        table.dropna(how='any',inplace= True)       
        return table
    
    def clean_orders_data(self, table):
        '''This method cleans the orders table by dropping the relevant columns and getting rid of
        any null values'''
        table.drop(columns='1',inplace=True)
        table.drop(columns='first_name',inplace=True)
        table.drop(columns='last_name',inplace=True)
        table.drop(columns='level_0',inplace=True)
        table.dropna(how='any',inplace= True)
        return table
    
    def clean_date_time(self, table):
        '''This method gets rid of any null values, converts time stamp to correct format and
        makes sure all formats in dates are numeric'''
        table['month'] = pd.to_numeric( table['month'],errors='coerce', downcast="integer")
        table['year'] = pd.to_numeric( table['year'], errors='coerce', downcast="integer")
        table['day'] = pd.to_numeric( table['day'], errors='coerce', downcast="integer")
        table['timestamp'] = pd.to_datetime(table['timestamp'], format='%H:%M:%S', errors='coerce')
        table.dropna(how='any',inplace= True)
        table.reset_index(inplace=True)       
        return table