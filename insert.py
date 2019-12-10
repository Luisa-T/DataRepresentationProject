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
sql = "INSERT INTO books()"
values = ()

cursor.execute(sql, values)

db.commit()
print("x record inserted", cursor.lastrowid)