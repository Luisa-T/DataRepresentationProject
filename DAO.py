# Importing the necessary packages
import mysql.connector
#import config as cfg

# Python anywhere database I created
class DAO():
    db=""
    def __init__(self): 
        self.db = mysql.connector.connect(
        host="LuTi.mysql.pythonanywhere-services.com",
        user="LuTi",
        password="D@t@rep19",
        database="LuTi$Library"
        )

    # Defining how to connect to the database
    #db = mysql.connector.connect(
     #   host = cfg.mysql['host'],
      #  user = cfg.mysql['user'],
       # password = cfg.mysql['password'],
        #database = cfg.mysql['database']
    #)
    

    cursor = db.cursor()

    cursor.execute("CREATE DATABASE LibraryProject")

    # Create a new entry into the database
    def create(self, values):
        cursor = self.db.cursor()
        sql = "INSERT INTO Books(Author, Title, Genre, Owned_by, format) values (%s, %s, %s, %s, %s)"
        values = ()

        cursor.execute(sql, values)

        self.db.commit()
        print("Record inserted", cursor.lastrowid)

    # Show all entries in the database
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

    # Find a book by the ID assigned to it
    def findByID(self, id):
        cursor = self.db.cursor()
        sql="select * from book where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDictionary(result)

    # Update an existing entry
    def update(self, values):
        cursor = self.db.cursor()
        sql="update Books set Author = %s, Title = %s, Genre = %s, Owned_by = %s, Format = %s, where id = %s"
        values = (id)

        cursor.execute(sql, values)

        self.db.commit()
        print("update done")

    # Deleting an entry
    def delete(self, id):
        cursor = self.db.cursor()
        sql="delete from Books where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.db.commit()
        print("delete complete")

    # This ensures that a new entry is added to the dictionary and is added to the database
    def convertToDictionary(self, result):
        colnames=['id', 'Author', 'Title','Genre', 'Owned by', 'Format']
        item = {}
            
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
            
        return item
            
    DAO = DAO()