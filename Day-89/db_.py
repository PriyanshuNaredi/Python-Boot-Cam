
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
import os
basedir = os.path.abspath(os.path.dirname(__file__))
basedir = f'{basedir}\instance'

app = Flask(__name__)

class Base(DeclarativeBase):
  pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'to-do.db')
db = SQLAlchemy(model_class=Base)
db.init_app(app)

@app.route("/")
def home():
    return render_template("index.html")





if __name__ == "__main__":
    app.run(debug=True)


#-------------------- https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/quickstart/#configure-the-extension
# # SQLite code snippet

# import sqlite3

# db = sqlite3.connect("books-collection.db")

# cursor = db.cursor()

# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")

# db.commit()