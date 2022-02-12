import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="", database="collage")

A=mydb.cursor()

A.execute("select * from bsc")

result=A.fetchall()

for i in result:

	print(i)


A.execute('select name from bsc')

ok=A.fetchall()

for i in ok:
	print(i)