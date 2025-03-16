import pandas as pd
from pymongo import MongoClient
import os

# MongoDB connection details
mongo_uri = "mongodb://localhost:27017/"
db_name = "job"
collection_name = "job"

# Path to Excel file
xls_file = "C:/Users/HP/Downloads/cleaned_data.xls"

# Check if file exists
if not os.path.exists(xls_file):
    print(f"Error: The file '{xls_file}' does not exist.")
elif os.stat(xls_file).st_size == 0:
    print(f"Error: The file '{xls_file}' is empty.")
else:
    try:
        # Read Excel file
        df = pd.read_excel(xls_file, engine="xlrd")  # Use xlrd for .xls files

        # Check if DataFrame is empty
        if df.empty:
            print(f"Error: The file '{xls_file}' has no data to import.")
        else:
            # Connect to MongoDB
            # client = MongoClient(mongo_uri)
            client = MongoClient('mongodb+srv://wangchongye125:test123456@cluster0.of7cz.mongodb.net/job?retryWrites=true&w=majority&appName=Cluster0')
            db = client[db_name]
            collection = db[collection_name]

            # Insert data into MongoDB
            collection.insert_many(df.to_dict(orient="records"))

            print("Excel data successfully inserted into MongoDB!")

    except pd.errors.EmptyDataError:
        print(f"Error: No columns to parse from the file '{xls_file}'.")
    except Exception as e:
        print(f"An error occurred: {e}")