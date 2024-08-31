import pandas as pd
import mysql.connector



conn =mysql.connector.connect(host='localhost',user='root',password='2953',database='db1')

query = "SELECT * FROM tb1;"  # replace with your table name

# Fetch data into a pandas DataFrame
df = pd.read_sql(query, conn)

# Export to CSV
df.to_csv('output_file.csv', index=False)  # Replace 'output_file.csv' with your desired filename

# Optionally, export to Excel
df.to_excel('output_file.xlsx', index=False)  # Replace 'output_file.xlsx' with your desired filename



conn.close()