import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root', passwd='',database='mydatabase')

A=mydb.cursor()

sql="INSERT INTO ba(sid,name,rollno,result,marks) values(%s,%s,%s,%s,%s)"
val=('3','amit','123412','pass','342')

A.execute(sql,val)

mydb.commit()

print("row inserted, sid:",A.lastrowid)