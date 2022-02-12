import mysql.connector
 
mydb=mysql.connector.connect(host="localhost",user="root",passwd='',database='mydatabase')

A=mydb.cursor()

sql=('select * from ba order by name desc')

A.execute(sql)

result=A.fetchall()

for i in result:
	print(i)