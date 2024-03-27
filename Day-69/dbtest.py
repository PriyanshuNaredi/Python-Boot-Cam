from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func

import os
basedir = os.path.abspath(os.path.dirname(__file__))
print(f'{basedir}\instance')

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] =\
#         'sqlite:///' + os.path.join(basedir, 'database.db')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)


# class Student(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     firstname = db.Column(db.String(100), nullable=False)
#     lastname = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(80), unique=True, nullable=False)
#     age = db.Column(db.Integer)
#     created_at = db.Column(db.DateTime(timezone=True),
#                            server_default=func.now())
#     bio = db.Column(db.Text)

#     def __repr__(self):
#         return f'<Student {self.firstname}>'

# if __name__ == "__main__":
#     app.run()
# from sqlalchemy import create_engine
# # define your database credentials

# # using credentials create engine object
# engine = create_engine(f'mysql + pymysql:// {user}: {password}@{host}:{port}/{database}')
# # checking if the connection is made
# try:
#     with engine.connect() as conn:
#         print(f" Successfully Connected to the database:")
# except Exception as ex:
#     print(f" Sorry Could not connect to the database: {ex}")