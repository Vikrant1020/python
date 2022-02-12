import mysql.connector
 
mydb=mysql.connector.connect(host='localhost',user='root',passwd='',database='mydatabase')

A=mydb.cursor()

#sql="update ba set result='pass' where name='vikrant'"
sql="update ba set sid='%s' where marks='%s'"
adr=('5','654')

A.execute(sql)

mydb.commit()

print(A.rowcount,'records affected')