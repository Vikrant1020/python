import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='',database='mydatabase')
A=mydb.cursor()

sql="SELECT * FROM ba limit 3 offset 1"

A.execute(sql)

result=A.fetchall()

for i in result:
	print(i)