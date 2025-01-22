# Multinational Retail Data Centralisation

In this project we create a postresql database locally, then create multiple classes to create, process and clean the data from various sources, and then run sql queries to imitate real life scenarios.

Key technologies used are python, AWS(S3), pandas, sqlalchemy and yaml.

## Project Modules

1. Database_Utils: In the 'database_utils.py' file we establish the connection between the database and the local host using the credentials within the yaml file.

2. Data_Cleaning: In the 'data_cleaning.py' file we convert the table to a dataframe and start cleaning the data using the pandas library. Looking out for any anomilies and extracting any null values within the table.
