import mysql.connector
import config as cfg

class DAO():
    db=""
    def __init__(self): 
        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        #user="datarep",  # this is the user name on my mac
        #passwd="password" # for my mac
        database="datarepresentation"
        )

    db = mysql.connector.connect(
        host = cfg.mysql['host'],
        user = cfg.mysql['user'],
        password = cfg.mysql['password'],
        database = cfg.mysql['database']
    )
    #set FLASK_ENV=development

    cursor = db.cursor()

    cursor.execute("CREATE DATABASE LibraryProject")

    def create(self, values):
        cursor = self.db.cursor()
        sql = "INSERT INTO Books(Author, Title, Genre, Owned_by, format) values (%s, %s, %s, %s, %s)"
        values = ()

        cursor.execute(sql, values)

        self.db.commit()
        print("x record inserted", cursor.lastrowid)

    def displayAll(self):
        cursor = self.db.cursor()
        sql="select * from Books"
        values = ()
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))

        return returnArray

    def findByID(self, id):
        cursor = self.db.cursor()
        sql="select * from book where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDictionary(result)

    def update(self, values):
        cursor = self.db.cursor()
        sql="update Books set Author = %s, Title = %s, Genre = %s, Owned_by = %s, Format = %s, where id = %s"
        values = (id)

        cursor.execute(sql, values)

        self.db.commit()
        print("update done")

    def delete(self, id):
        cursor = self.db.cursor()
        sql="delete from Books where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.db.commit()
        print("delete complete")

    def convertToDictionary(self, result):
        colnames=['id', 'Author', 'Title','Genre', 'Owned by', 'Format']
        item = {}
            
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
            
        return item
            
    DAO = DAO()