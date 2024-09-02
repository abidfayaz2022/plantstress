import mysql.connector

# Connect to MySQL using PyMySQL
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='2953',
    database='Plant_Stress_Resistance'
)

cursor = connection.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("Database version:", data)

connection.close()
