import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('STAFF.db')

# Define table_name and attribute_list for INSTRUCTOR table
table_name = 'INSTRUCTOR'
attribute_list = ['ID', 'FNAME', 'LNAME', 'CITY', 'CCODE']

# Read data from CSV file into a pandas DataFrame
file_path = './INSTRUCTOR.csv'
df = pd.read_csv(file_path, names=attribute_list)

# Write DataFrame to SQLite table (replace if exists)
df.to_sql(table_name, conn, if_exists='replace', index=False)

# Query and print all data from the INSTRUCTOR table
query_statement = f"SELECT * FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)


# Function to count rows in a table and print the count
def count_db(table):
    query_statement = f"SELECT COUNT(*) FROM {table}"
    query_output = pd.read_sql(query_statement, conn)
    print(query_statement)
    print(query_output)


# Count rows in the INSTRUCTOR table
count_db(table_name)

# Append new data to the INSTRUCTOR table
data_dict = {'ID': [100], 'FNAME': ['John'], 'LNAME': ['Doe'], 'CITY': ['Paris'], 'CCODE': ['FR']}
data_append = pd.DataFrame(data_dict)
data_append.to_sql(table_name, conn, if_exists='append', index=False)
print('Data appended successfully')

# Count rows in the INSTRUCTOR table after appending data
count_db(table_name)

# Define table2 and attribute_list2 for Departments table
table2 = "Departments"
attribute_list2 = ['DEPT_ID', 'DEP_NAME', 'MANAGER_ID', 'LOC_ID']

# Read data from Departments.csv into a pandas DataFrame
file_path2 = './Departments.csv'
df2 = pd.read_csv(file_path2, names=attribute_list2)

# Write DataFrame to SQLite table Departments (replace if exists)
df2.to_sql(table2, conn, if_exists='replace', index=False)

# Append new data to the Departments table
data_dict2 = {'DEPT_ID': [9], 'DEP_NAME': ['Quality Assurance'], 'MANAGER_ID': [30010], 'LOC_ID': ['L0010']}
data_append = pd.DataFrame(data_dict2)
data_append.to_sql(table2, conn, if_exists='append', index=False)
print('Data appended successfully')

# Query and print all data from the Departments table
query_statement = f"SELECT * FROM {table2}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# Query and print only DEP_NAME column from the Departments table
query_statement = f"SELECT DEP_NAME FROM {table2}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# Count rows in the Departments table
count_db(table2)

# Close the SQLite connection
conn.close()
