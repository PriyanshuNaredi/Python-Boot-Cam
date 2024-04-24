import random
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TimeField, SelectField
from wtforms.validators import DataRequired, URL
import csv
from flask_bootstrap import Bootstrap5
import os
basedir = os.path.abspath(os.path.dirname(__file__))
basedir = f'{basedir}\instance'



app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'cafes.db')
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        #Method 1. 
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            #Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary
        
        #Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}



@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record

# @app.route("/random")
# def get_random_cafe():
#     result = db.session.execute(db.select(Cafe))
#     all_cafes = result.scalars().all()
#     random_cafe = random.choice(all_cafes)
#     return jsonify(cafe={
#         #Omit the id from the response
#         # "id": random_cafe.id,
#         "name": random_cafe.name,
#         "map_url": random_cafe.map_url,
#         "img_url": random_cafe.img_url,
#         "location": random_cafe.location,
        
#         #Put some properties in a sub-category
#         "amenities": {
#           "seats": random_cafe.seats,
#           "has_toilet": random_cafe.has_toilet,
#           "has_wifi": random_cafe.has_wifi,
#           "has_sockets": random_cafe.has_sockets,
#           "can_take_calls": random_cafe.can_take_calls,
#           "coffee_price": random_cafe.coffee_price,
#         }
#     })

@app.route("/random")
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)
    #Simply convert the random_cafe data record to a dictionary of key-value pairs. 
    return jsonify(cafe=random_cafe.to_dict())

@app.route("/all")
def get_all_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    return render_template('cafes.html',cafes=[cafe.to_dict() for cafe in all_cafes])

@app.route("/search/loc=<loc>") # My Way
def my_get_cafe_at_location(loc):
    result = db.session.execute(db.select(Cafe).where(Cafe.location == loc))
    all_cafes = result.scalars().all()
    
    if all_cafes:
        return jsonify(cafes=[cafe.to_list() for cafe in all_cafes])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404

@app.route("/search",methods=["GET", "POST"]) # Angela Way
def get_cafe_at_location():
    if request.method == "POST":
        query_location = request.args.get("loc")
        result = db.session.execute(db.select(Cafe).where(Cafe.location == query_location))
        # Note, this may get more than one cafe per location
        all_cafes = result.scalars().all()
        if all_cafes:
            return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])
        else:
            return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404
    return render_template("index.html")

# HTTP POST - Create Record
def str_to_bool(v):
    if v in ['True', ' true', 'T', 't', 'Yes', 'yes', 'y', '1']:
        return True
    else:
        return False


@app.route("/add", methods=["GET", "POST"])
def add_a_cafe():
    new_cafe = Cafe(name=request.form["name"],
                    map_url=request.form["map_url"],
                    img_url=request.form["img_url"],
                    location=request.form["location"],
                    seats=request.form["seats"],
                    has_toilet=str_to_bool(request.form["has_toilet"]),
                    has_wifi=str_to_bool(request.form["has_wifi"]),
                    has_sockets=str_to_bool(request.form["has_sockets"]),
                    can_take_calls=str_to_bool(request.form["can_take_calls"]),
                    coffee_price=request.form["coffee_price"]
                    )
    db.session.add(new_cafe)
    db.session.commit()

    return jsonify(response={"success": "Successfully added the new cafe"})

# HTTP PUT/PATCH - Update Record

#Patch 
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def patch_new_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.get_or_404(Cafe,cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."})
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."})

# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == "TopSecretKey":
        cafe = db.get_or_404(Cafe,cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403

if __name__ == '__main__':
    app.run(debug=True)
