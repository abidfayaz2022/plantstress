import mysql.connector
conn =mysql.connector.connect(host='localhost',user='root',password='2953',database='d1')
print(conn.connection_id)
#to perform any sql command create object of cursor function
cur = conn.cursor()
# cur.execute("CREATE DATABASE db1")
# cur.execute("create table tb1(id INT(4),title varchar(20) )")

i=0
while i<32400:
    i=i+1
    cur.execute("INSERT INTO t1 (name) VALUES (%s)", ("python3"))
  


conn.commit()

    
cur.close()
conn.close()