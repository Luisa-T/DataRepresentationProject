import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    #user="Luisa"
    #password=""
    database="LibraryProject"
)

cursor = db.cursor()
sql="select * from books where "
values = ()

cursor.execute(sql, values)
result= cursor.fetchall()
for x in result:
    print