from flask import Flask, jsonify, request, abort

app= Flask(_name_, static_url_path='', static_folder='.')

books=[{"id":1, "title": "", "Author", "", "ISBN", "Pice"}]
nextID = 0
@app.route('/books')
def getAll():
    return "you want to get the book with " + str(id)


@app.route()
def createBook(id):
    if not request.json:
        abort(400)
    #other checking, duplicate checking
    book = {
        "id": nextID,
        "Title": request.json['Title'],
        "Author": request.json['Title'],
        "Title": request.json['Title']
        "Title": request.json['Title']
    }
    nextId +=1
    books.append(book)
    return jsonify(book)

@app.route('/books', methods=['POST'])
def findBook(id):
    foundBook = list(filter(lambda t: t['id'] == id, books))
    if len(foundBooks) == 0:
        return jsonify({}), 204
    else:
    return jsonify(foundBooks[0]) + str(id)


@app.route('/book/<int:id>', methods=['UPDATE'])
def updateBook(id):
    foundBooks = list(filter(lambda t: t['id'] == id, books))
    if(len(foundBooks) == 0):
        abort(404)
    foundBooks = foundBooks[0]
    if not request.json:
        abort(400)
    else:
        reqJson = request.json
    if 'Price' in reqJson and type(reqJson['Price']) is not int:
        abort(400)
    if 'Title' in reqJson:
        foundBook['Title'] = reqJson['Title']
    if 'Title' in reqJson:
        foundBook['Title'] = reqJson['Title']
    if 'Title' in reqJson:
        foundBook['Title'] = reqJson['Title']
    if 'Title' in reqJson:
        foundBook['Title'] = reqJson['Title']
    return "you want to get the book with " + str(id)

@app.route('/book/<int:id>', methods=['DELETE'])
def deleteBook(id):
    return "you want to get the book with " + str(id)
    foundBooks = list(filter(lambda t: t['id'] == id, books))
    if(len(foundBooks) == 0):
        abort(404)
    books.remove(foundBooks[0])
    return jsonify({"complete":True})

if __name__ == '__main__' :
    app.run(debug=True)