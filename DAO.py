import mysql.connector
import config as cfg
db = mysql.connector.connect(
    host = cfg.mysql['host'],
    user = cfg.mysql['user'],
    password = cfg.mysql['password'],
    database = cfg.mysql['database']
)
#set FLASK_ENV=development

cursor = db.cursor()

cursor.execute("CREATE DATABASE LibraryProject")

def insert():
    sql = "INSERT INTO books()"
    values = ()

    cursor.execute(sql, values)

    db.commit()
print("x record inserted", cursor.lastrowid)

def displayAll():
    cursor = db.cursor()
    sql="select * from books where "
    values = ()

    cursor.execute(sql, values)
    result= cursor.fetchall()
    for values in result:
        print

def update():
    cursor = db.cursor()
    sql="update books set "
    values = ()

    cursor.execute(sql, values)

    db.commit()
    print("update done")

def delete():
    cursor = db.cursor()
    sql="delete from books where "
    values = ()

    cursor.execute(sql, values)

    db.commit()
    print("update delete")