import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="mydatabase")

A=mydb.cursor()

# for creating a new database.
A.execute("CREATE DATABASE mydatabase")

# for checking all database's
A.execute("SHOW DATABASES")

for i in A:
	print(i)

# for creating a table in database. create table must be in capitale letters
A.execute("CREATE TABLE ba( Sid int(5), name varchar(255), rollno int(11), result varchar(4))")

# for adding primary key in a coloum
A.execute("CREATE TABLE bcom( id int AUTO_INCREMENT PRIMARY KEY, name varchar(255), rollno int(11), result varchar(4))")


#for checking tables exixting.
A.execute("show tables")
print("\n\n")
for i in A:
	print(i)

A.execute("ALTER TABLE ba add column marks int(3)")


#for fetch data from a table
A.execute('select name from ba')

B=A.fetchall()

for i in B:
	print(i)

