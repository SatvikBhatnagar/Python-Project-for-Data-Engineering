import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup

# URL of the webpage containing the film data
url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'

# Name of the SQLite database and table to be used
db_name = 'Movies.db'
table_name = 'Top_50'

# File path to save the CSV file
csv_path = './top_50_films.csv'

# Initialize an empty DataFrame with specified columns
df = pd.DataFrame(columns=["Film", "Year", "Rotten Tomatoes' Top 100"])

# Fetch HTML content from the specified URL
html_page = requests.get(url).text

# Parse HTML using BeautifulSoup
data = BeautifulSoup(html_page, 'html.parser')

# Find all tables within the HTML data
tables = data.find_all('tbody')

# Select the first table (assuming it contains the desired film data)
rows = tables[0].find_all('tr')

# Iterate through rows in the table to extract film information
count = 0
for row in rows:
    if count < 25:  # Limit to 25 films
        col = row.find_all('td')
        if len(col) != 0:
            # Extract data for each film and create a DataFrame row
            data_dict = {"Film": col[1].contents[0],
                         "Year": int(col[2].contents[0].strip()),
                         "Rotten Tomatoes' Top 100": col[3].contents[0]}
            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df, df1], ignore_index=True)
            count += 1
    else:
        break  # Exit loop after 25 films

# Save the extracted film data to a CSV file
df.to_csv(csv_path)

# Connect to the SQLite database
conn = sqlite3.connect(db_name)

# Write the film data DataFrame to a SQLite table (replace if exists)
df.to_sql(table_name, conn, if_exists='replace', index=False)

# Close the SQLite connection
conn.close()
