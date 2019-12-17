# DataRepresentationProject

This file gives a summary of the project and the files written for it. It also contains instructions on how to run these files

## 1. LibraryLuisaTimothy.html
This is the Browser interface for the project. Basic CRUD operations are within Using the DOM and Javascript, as well as Ajax at the bottom of the file.

## 2. serverflask.py
This contains the Python code for the flask server. The code provides the CRUD functionalities, with some basic duplicate checking.

## 3. DAO.py
This file attempts to connect the the PythonAnywhere Database created for this project. The code also contains the CRUD operations using SQL commands.
I have split up the CRUD operations in SQL into different files as well which are also included
#### 3.1 insert.py
#### 3.2 displayAll.py
#### 3.3 updating.py
#### 3.4 update.py
#### 3.5 updateDelete.py
#### 3.6 delete.py


## 4. projectLuisaTimothy.py
This file contains the SQLAlchemy code to create the Database table, as well as CRUD operations and the Flask code is also added.

## 5. dbconfig.py
This file contains the information to connect to the PythonAnywhere Database.

## 6. Curl
For the convenience of the reader I am including the CRUL commands here so that they can be copied and pasted.

#### 6.1 Display all
curl -i http://localhost:5000/Books

#### 6.2 Find by ID
curl -i http://localhost:5000/Books/2

#### 6.3 Create
curl -i -H "Content-Type:application/json" -X POST - d '{"Author": "Agatha Christie", "Title": "Sparkling Cyanide", "Genre": "Crime", "Owned by": "Yourself", "Format": "Hardback"}' http://localhost:5000/Books

#### 6.4 Update
curl -i -H "Content-Type:application/json" -X PUT - d '{"Format":"Audiobook"}' http://localhost:5000/Books/Agatha%Christie

#### 6.5 Delete
curl -i -X DELETE http://localhost:500/Books/Steve%Cavanagh


