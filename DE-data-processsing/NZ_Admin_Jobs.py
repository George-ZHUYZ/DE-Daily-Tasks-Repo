import numpy as np
import pandas as pd
import os

# Read the raw data from the dataset file with .xlsx extension,
# and print the brief description of the dataset.
filePath = './NZ_Admin_JOBS.xlsx'
rawData = pd.read_excel(filePath)
print("NZ_Admin_Jobs data summary: \n", rawData.describe())
nRow, nCol = rawData.shape
print("NZ_Admin_Jobs data rows: \n", nRow)
print("NZ_Admin_Jobs data columns: \n", nCol)

'''
After reading the dataset, get the initial idea on how to clean and preprocess the raw data
1. Rename the column header with proper title.
2. Fill the empty cell with "Unknown" text.
3. Check the sixth column that displays the classification of the role,
    and transfer any data not beginning with "Classification:" into the new column, which lists the related salary.
    Then fill "Unknown" text in the corresponding cell.
4. Sort the dataset by Role Name alphabetically, and having salary info comes first.
'''
print(list(rawData))
rawData.rename(columns={'字段1': 'Role Name',
                        '字段1_link': 'Role Link',
                        '字段2': 'Company Name',
                        '字段3': 'Role Location',
                        '字段4': 'Publish Date',
                        '字段5': 'Role Classification'}, inplace=True)
print(rawData.columns)

# Fill NaN values with Unknown text
rawData.fillna('Unknown', inplace=True)

#
rawData['Role Salary'] = 'Unknown'
for row in range(1, len(rawData)):
    tmpTxt = rawData.iloc[row, 5]
    if 'classification' not in tmpTxt:
        rawData.iloc[row, 6] = tmpTxt
        rawData.iloc[row, 5] = 'Unknown'

# Sort the dataset
# TO-DO: Need to fix the multiple columns sorting issue
outputData = rawData.sort_values([rawData.columns[0], rawData.columns[6]], ascending=[True, False])

# Write the data being initial processed to the new file
newFilePath = './New_NZ_Admin_JOBS.xlsx'
if os.path.exists(newFilePath):
    os.remove(newFilePath)

outputData.to_excel(newFilePath, sheet_name='after_1st_processed')
