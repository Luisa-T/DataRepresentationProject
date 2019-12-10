import mysql.connector

class StudentDAO:
    db = ""
def __init__(s module mysql
    self.db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
        #user="Luisa",
        #password="",
    database="LibraryProject"
    ))
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    #user="Luisa",
    #password="",
    database="LibraryProject"
)

cursor = db.cursor()
sql="update books set "
values = ()

cursor.execute(sql, values)

db.commit()
print("update done")