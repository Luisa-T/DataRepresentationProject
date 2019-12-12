from flask import Flask, jsonify, request, abort
import sqlalchemy
from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo=True)
from sqlalchemy.ext.declarative import declarative_base, Column, Integer, String, Sequence, sessionmaker

class Books(Base):
    __tablename__ = 'Books'
    id = Column(Integer, Sequence('Book_id_seq'), primary_key=True)
    Author = Column(String)
    Title = Column(String)
    Genre = Column(String)
    Owned_by = Column(String)
    Format = Column(String)

    def __repr__(self):
        return "<Books(author='%s', Title='%s', Genre='%s', Owned_by='%s', Format='%s')>" % (self.Author, self.Title, self.Genre, self.Owned_by, self.Format)

Base = declarative_base()

Books.__table__ 
Table('Books', MetaData(bind=None), 
    Column('id', Integer(), table=Books, primary_key=True, nullable=False),
    Column('Author', String(), table=Books),
    Column('Title', String(), table=Books),
    Column('Genre', String(), table=Books),
    Column('Owned_by', String(), table=Books),
    Column('Format', String(), table=Books), schema=None)

Base.metadata.create_all(engine)
SELECT 
PRAGMA table_info("Books")
()
PRAGMA temp.table_info("Books")
()
CREATE TABLE Books (
    id INTEGER NOT NULL, name VARCHAR,
    Author VARCHAR,
    Title VARCHAR,
    Genre VARCHAR,
    Owned_by VARCHAR,
    Format VARCHAR,
    PRIMARY KEY (id)
)
()
COMMIT
)

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()



app= Flask(__name__, static_url_path='', static_folder='.')

#create many
session.add_all(Books=[{"id":1, " Author": "Moshin Hamid", "Title": "Moth Smoke", "Genre": "Contemporary Fiction", "Owned by": "yourself", "Format": "Paperback"},
{"id":2, " Author": "Andrea Camilleri", "Title": "Blade of Light", "Genre": "Crime", "Owned by": "yourself", "Format": "Paperback"},
{"id":3, " Author": "Margaret Atwood", "Title": "Hag-Seed", "Genre": "Contemporary Fiction", "Owned by":"Library", "Format": "Hardback"},
{"id":4, " Author": "Elena Ferrante", "Title": "Tage des Verlassenwerdens", "Genre": "Contemporary Fiction", "Owned by": "yourself", "Format": "Audiobook"},
{"id":5, " Author": "Clare Fisher", "Title": "All the Good Things", "Genre": "Contemporary Fiction", "Owned by":"Library", "Format": "E-Audiobook"},
{"id":6, " Author": "Salman Rushdie", "Title": "The Golden House", "Genre": "Contemporary Fiction", "Owned by":"Yourself", "Format": "Hardback"},
{"id":7, " Author": "Andrea Camilleri", "Title": "The Potter's Field", "Genre": "Crime", "Owned by":"Yourself", "Format": "Paperback"},
{"id":8, " Author": "", "Title": "Machine Learning For Dummies", "Genre": "Textbook", "Owned by":"Yourself", "Format": "Paperback"},
{"id":9, " Author": "J. K. Rowling", "Title": "Harry Potter and the Deathly Hallows", "Genre": "Contemporary Fiction", "Owned by": "Yourself", "Format": "Hardback"},
{"id":10, " Author": "Elena Ferrante", "Title": "Meine Geniale Freundin", "Genre": "Contemporary Fiction", "Owned by": "Yourself", "Format": "Hardback"},
{"id":11, " Author": "", "Title": "Forensic Psychology", "Genre": "Textbook", "Owned by": "Yourself", "Format": "Paperback"},
{"id":12, " Author": "Melanie Raabe", "Title": "The Stranger Upstairs", "Genre": "Crime", "Owned by": "Library", "Format": "E-Audiobook"},
{"id":13, " Author": "", "Title": "Python For Dummies", "Genre": "Non-Fiction", "Owned by": "Yourself", "Format": "Paperback"},
{"id":14, " Author": "Donna Leon", "Title": "Beastly Things", "Genre": "Crime", "Owned by": "Yourself", "Format": "Hardback"},
{"id":15, " Author": "Charles Dickens", "Title": "Great Expectations", "Genre": "Classics", "Owned by": "Yourself", "Format": "Ebook"},
{"id":16, " Author": "Ben Aaronovich", "Title": "Moon Over Soho", "Genre": "Crime", "Owned by": "Yourself", "Format": "Paperback"},
{"id":17, " Author": "Michael Ende", "Title": "Die Unendliche Geschichte", "Genre": "Classics", "Owned by": "Yourself", "Format": "Hardback"},
{"id":18, " Author": "Martha Grimes", "Title": "Jerusalem Inn", "Genre": "Crime", "Owned by": "Yourself", "Format": "Paperback"},
{"id":19, " Author": "John Marrs", "Title": "The Passengers", "Genre": "Crime", "Owned by": "Yourself", "Format": "Paperback"},
{"id":20, " Author": "Hakan Nesser", "Title": "Die Einsamen", "Genre": "Crime", "Owned by": "Yourself", "Format": "Hardback"},
{"id":21, " Author": "Richard Shepherd", "Title": "Unnatural Causes", "Genre": "Non-Fiction", "Owned by": "Yourself", "Format": "Hardback"}])

session.commit()
# create one
JP_Book = Books(Author='James Patterson', Title='Kiss The Girls', Genre='Crime', Owned_by='Yourself', Format='Paperback')
session.add(JP_Book)

# select one
session.query(Books).filter(Books.Author.in_(['James Patterson', 'Kiss the Girls', 'Crime', 'Yourself', 'Paperback'])).all()
[Books(Author='James Patterson', Title='Kiss The Girls', Genre='Crime', Owned_by='Yourself', Format='Paperback')]

for instance in session.query(Books).order_by(Books.id):
    print()
# another example of select one
for Books in session.query(Books).\
        filter(Books.Author=='Andrea Camilleri').\
        filter(Books.Title=='Blade of Light'):
    print(Books)

session.query(Books).from_statement(
    text("SELECT * FROM users where name=:name")).\
    params(name='ed').all()
# update
session.dirty
IdentitySet([Books(Author='James Patterson', Title='Kiss The Girls', Genre='Crime', Owned_by='Yourself', Format='Paperback')])

#delete
session.delete('James Patterson')
session.query(Books).filter_by(Author='James Patterson').count()

global nextID
nextID = 0
@app.route('/books')
def getAll():
    return "In you current library" + str(id)


@app.route()
def createBook(id):
    if not request.json:
        abort(400)
    if Books (filter(lambda t: t['Author' == 'Author']) and (lambda t: t['Title'] == 'Title')):
        return jsonify("You already have this one ") + Books
    #other checking, duplicate checking
    book = {
        "id": nextID,
        "Author": request.json['Author'],
        "Title": request.json['Title'],
        "Genre": request.json['Genre'],
        "Owned by": request.json['Owned by'],
        "Format": request.json['Format']
    }
    nextID +=1
    Books.append(book)
    return jsonify(book)

@app.route('/books', methods=['POST'])
def findBooks(id):
    foundBooks = list(filter(lambda t: t['id'] == id, Books))
    if len(foundBooks) == 0:
        return jsonify({}), 204
    else:
        return jsonify(foundBooks[0]) + str(id)


@app.route('/books/<int:id>', methods=['UPDATE'])
def updateBook(id):
    foundBooks = list(filter(lambda t: t['id'] == id, Books))
    if(len(foundBooks) == 0):
        abort(404)
    foundBooks = foundBooks[0]
    if not request.json:
        abort(400)
    else:
        reqJson = request.json
    if 'Author' in reqJson and type(reqJson['Author']) is not str:
        abort(400)
    if 'Title' in reqJson:
        foundBooks['Title'] = reqJson['Title']
    if 'Genre' in reqJson:
        foundBooks['Genre'] = reqJson['Genre']
    if 'Owned by' in reqJson:
        foundBooks['Owned by'] = reqJson['Owned by']
    if 'Format' in reqJson:
        foundBooks['Format'] = reqJson['Format']
    return "you want to get the book with " + str(id)

@app.route('/book/<int:id>', methods=['DELETE'])
def deleteBook(id):
    return "you want to get the book with " + str(id)
    foundBooks = list(filter(lambda t: t['id'] == id, Books))
    if(len(foundBooks) == 0):
        abort(404)
    Books.remove(foundBooks[0])
    return jsonify({"complete":True})

if __name__ == '__main__' :
    app.run(debug=True)