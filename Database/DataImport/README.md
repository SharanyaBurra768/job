Table of Contents
- Overview
- Configuration
- Installation
- Error Handling
- License

Overview
This script reads data from an Excel file (`.xls`) and inserts it into a MongoDB database. It ensures error handling for missing or empty files and verifies that the Excel sheet contains data before importing.

Configuration
MongoDB Connection
Modify the following parameters in the script if needed:
```python
mongo_uri = "mongodb://localhost:27017/"
db_name = "job"
collection_name = "job"
```
For MongoDB Atlas, replace `mongo_uri` with your connection string.

Dataset
- File Name: `cleaned_data.xls`
- Format: Excel (`.xls`)
- Encoding: UTF-8

Installation
Install the required libraries:
```sh
pip install pandas pymongo xlrd
```

Error Handling
The script checks for the following:
- If the file does not exist, it prints an error message.
- If the file is empty, it notifies the user.
- If the DataFrame is empty, it warns about no data to import.
- If any other error occurs during execution, it is caught and displayed.

License
This project is open-source and can be modified as needed.

