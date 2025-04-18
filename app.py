from flask import Flask, render_template

app = Flask(__name__)

# Datos de ejemplo
books = [
    {'title': '2012', 'author': 'George Orwell'},
    {'title': 'To Kill a Polar Bear', 'author': 'Harper Lee'},
    {'title': 'The Great Swordsman', 'author': 'F. Scott Fitzgerald'}
]

authors = ['George Orwell', 'Harper Lee', 'F. Scott Fitzgerald']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/books')
def book_list():
    return render_template('books.html', books=books)

@app.route('/authors')
def author_list():
    return render_template('authors.html', authors=authors)

if __name__ == '__main__':
    app.run(debug=True)
