from flask import Flask, request, jsonify

app = Flask(__name__)

#Data lake
books = []
authors = []
categories = []

# Get all the books
@app.route('/books', method = ['GET'])
def get_books():
  return jsonify(book), 200

# add new books
@app.route('/books', method = ['POST'])
def add_book():
  data = request.json
    book = {
      "id": len(books) + 1,
      "title": data.get("title"),
      "author_id": data.get("author_id"),
      "category_id": data.get("category_id")
    }
  books.append(book)
  return jsonify(book), 201

# Get all the authors
@app.route('/authors', method = ['GET' ])
def get_authors():
  return jsonify(author), 200
  
# add new authors
@app.route('/authors', method = [['POST'])
def add_author():
  data = request.json
    author = {
      "id": len(authors) + 1
      "name": data.get("name")
    }
  authors.append(author)
  return jsonify(author), 200

# get all the categories
@app.route('/categories', method = ['GET'])
def get_categories():
  return jsonify(categories), 200

# add new categories
@app.route('/categories', method=['POST']) 
def add_category():
  data = request.json
    categories = {
      "id": len(categories) + 1
      "name": data.get("name")
    }
  categories.append(category)
  retrun jsonify(category), 201
  
if __name__ == '__main__':
  app.run(debug=True)




