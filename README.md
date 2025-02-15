# Multinational Retail Data Centralisation

In this project we create a postresql database locally, then create multiple classes to create, process and clean the data from various sources, and then run sql queries to imitate real life scenarios. My aim in this project is to learn how to retieve data from various locations and to get an understanding of multiple data types, creating relevance in applying these skills in real world applications.
So far I now have a greater understanding of python classes and its capabilities in turning complex code into something quite simple. I have also learnt how to connect data from vs code to pgadmin, in addition as a result of pursuing this project I now have a good amount of knowledge on regular expressions, tabula-py and boto3 libraries.

Key technologies used are python, AWS(S3), pandas, sqlalchemy, yaml, json, tabula-py, regex, numpy, boto3 and botocore.

## Project Modules

1. Database_Utils: In the 'database_utils.py' file we establish the connection between the database and the local host using the credentials within the yaml file.

2. Data_Cleaning: In the 'data_cleaning.py' file we convert the table to a dataframe and start cleaning the data using the pandas library. Looking out for any anomilies and extracting any null values within the table.

3. Data_Extraction: In the 'data_extraction.py' file we extract data from multiple locations, e.g. AWS S3, and extract the data from there to then clean said data.
