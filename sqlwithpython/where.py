import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',passwd='',database='mydatabase')

A=mydb.cursor()

#sql='select * from ba where rollno=123456'

#both "" '' must be used 
#sql="select * from ba where name like '%a%'"

sql="SELECT * from ba where name like '%a%'"
adr=("subh")
A.execute(sql,adr)

result=A.fetchall()

for i in result:
	print(i)