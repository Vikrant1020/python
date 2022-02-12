import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="mydatabase")

A=mydb.cursor()

# always use %s for every datatype.
sql=("INSERT INTO ba(sid,name,rollno,result,marks) values (%s,%s,%s,%s,%s)")
val=("1","vikrant","123456","pas","342")

A.execute(sql,val)

# will be excutded on database.
mydb.commit()

print(A.rowcount,"record inserted")

sql1=("INSERT INTO bcom(id, name, rollno, result) values(%s,%s,%s,%s)")
val1=[('1','rahul','12341','pass'),
('2','vivek','34213','fail')
]

A.executemany(sql1,val1)

mydb.commit()

print(A.rowcount,'record inserted')