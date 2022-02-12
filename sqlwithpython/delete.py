import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',passwd='',database='mydatabase')

A=mydb.cursor()

sql=("DELETE FROM ba WHERE  name ='amit'")

A.execute(sql)

mydb.commit()

reslut=A.fetchall()

for i in reslut:
	print(i)