from flask import Flask, jsonify, request, abort, make_response
from flask_cors import CORS
from DAO import DAO

app = Flask(__name__, static_url_path='', static_folder='.')
Books = []
nextID = id + 1
# Create
@app.route()
def createBooks():
    Books = []
    if not request.json:
        abort(400)
    # Checking if the book already exists in the table
    if Books (filter(lambda t: t['Author' == 'Author']) and (lambda t: t['Title'] == 'Title')):
        return jsonify("You already have this one ") + Books
    Books = {
        "id": nextID,
        "Author": request.json['Author'],
        "Title": request.json['Title'],
        "Genre": request.json['Genre'],
        "Owned_by": request.json['Owned_by'],
        "Format": request.json['Format']
    }
    nextID +=1
    Books.append(Books)
    return jsonify(Books)

# Find one
@app.route('/Books', methods=['POST'])
def findBooks(Author):
    foundBooks = list(filter(lambda t: t['Author'] == Author, Books))
    if len(foundBooks) == 0:
        return jsonify({}), 204
    else:
        return jsonify(foundBooks[0]) + str(id)

# Update
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
    return "Do you want to get the book with " + str(id)

# Delete
@app.route('/book/<int:id>', methods=['DELETE'])
def deleteBook(Author):
    return "you want to get the book with " + str(Author)
    foundBooks = list(filter(lambda t: t['Author'] == Author, Books))
    if(len(foundBooks) == 0):
        abort(404)
    Books.remove(foundBooks[0])
    return jsonify({"complete":True})


@app.errorhandler(404)
def not_found404(error):
    return make_response( jsonify( {'error':'Not found' }), 404)

@app.errorhandler(400)
def not_found400(error):
    return make_response( jsonify( {'error':'Bad Request' }), 400)

if __name__ == '__main__' :
    app.run(debug= True)