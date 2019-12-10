import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    #user="Luisa"
    #password=""
)

cursor = db.cursor()

cursor.execute("CREATE DATABASE LibraryProject")