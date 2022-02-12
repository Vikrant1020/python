import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',passwd='',database='mydatabase')

A=mydb.cursor()

#sql="drop table bcom"
sql="DROP TABLE IF EXISTS yes"

A.execute(sql)