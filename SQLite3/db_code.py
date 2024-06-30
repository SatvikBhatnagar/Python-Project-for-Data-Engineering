import sqlite3
import pandas as pd

conn = sqlite3.connect('STAFF.db')


table_name = 'INSTRUCTOR'
attribute_list = ['ID', 'FNAME', 'LNAME', 'CITY', 'CCODE']

file_path = './INSTRUCTOR.csv'
df = pd.read_csv(file_path, names = attribute_list)

df.to_sql(table_name, conn, if_exists = 'replace', index =False)

query_statement = f"SELECT * FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)
def count_db(table):
    query_statement = f"SELECT COUNT(*) FROM {table}"
    query_output = pd.read_sql(query_statement, conn)

    print(query_statement)
    print(query_output)

count_db(table_name)

data_dict = {'ID' : [100],
            'FNAME' : ['John'],
            'LNAME' : ['Doe'],
            'CITY' : ['Paris'],
            'CCODE' : ['FR']}
data_append = pd.DataFrame(data_dict)
data_append.to_sql(table_name, conn, if_exists = 'append', index =False)
print('Data appended successfully')

count_db(table_name)

table2 = "Departments"
attribute_list2 = ['DEPT_ID', 'DEP_NAME', 'MANAGER_ID', 'LOC_ID']

file_path2 = './Departments.csv'
df2 = pd.read_csv(file_path2, names = attribute_list2)
df2.to_sql(table2, conn, if_exists = 'replace', index =False)

data_dict2 = {'DEPT_ID' : [9], 'DEP_NAME' : ['Quality Assurance'], 'MANAGER_ID' : [30010], 'LOC_ID' : ['L0010']}
data_append = pd.DataFrame(data_dict2)
data_append.to_sql(table2, conn, if_exists = 'append', index =False)
print('Data appended successfully')

query_statement = f"SELECT * FROM {table2}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

query_statement = f"SELECT DEP_NAME FROM {table2}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

count_db(table2)