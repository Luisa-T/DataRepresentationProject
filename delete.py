cursor = self.db.cursor()
sql = "update book set name = % ..."
cursor.execute(sql, values)
self.db.commit()
def delete(self, id):
    cursor