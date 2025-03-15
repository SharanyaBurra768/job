# Data Cleaning on Job Dataset  
## Table of Contents  
1. [Overview](#overview)  
2. [Dataset](#Dataset)  
3. [Cleaning Steps](#Cleaning-Steps)  
4. [Installation](#installation)  


## Overview  
This ipynb file focuses on cleaning and preprocessing a job dataset to ensure data quality for further analysis. The dataset initially contained duplicate rows, missing values, and potential outliers. This notebook applies various data-cleaning techniques using **pandas** and **numpy** to make the dataset more reliable for analysis.  

## Dataset
- **File Name:** `680JobDatasSet.csv`  
- **Format:** CSV  
- **Encoding:** UTF-8  

## Cleaning Steps  
1. **Load Dataset**: Read the CSV file using `pandas`.  
2. **Remove Duplicates**: Check and drop duplicate rows.  
3. **Handle Missing Values**: Fill missing values with mean or remove missing data.  
4. **Detect Outliers**: Use statistical methods (IQR) to filter outliers.  
5. **Convert Date and Time format: Convert the expiry date to understandable date and time format. 

## Installation  
Install the required libraries:  
```bash
pip install pandas numpy openpyxl
```
