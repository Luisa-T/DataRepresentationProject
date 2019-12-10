import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    #user="Luisa",
    #password="",
    database="LibraryProject"
)

cursor = db.cursor()
sql="delete from books where "
values = ()

cursor.execute(sql, values)

db.commit()
print("update delete")