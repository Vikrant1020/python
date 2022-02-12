import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

mycursor = mydb.cursor()

# %s stand for string
# adr = name which will be delete.
sql = "DELETE FROM ba WHERE name = %s"
adr = ("vikrant", )

mycursor.execute(sql, adr)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")
