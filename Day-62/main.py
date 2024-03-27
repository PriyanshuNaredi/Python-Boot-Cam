from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TimeField, SelectField
from wtforms.validators import DataRequired, URL
import csv
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
  name     = StringField( label="name", validators=[ DataRequired() ] )
  location = StringField( label="location", validators=[ DataRequired(), URL() ] )
  
  open     = TimeField( label="open", format='%H:%M:%S',
                        render_kw={"step": "1"}, validators=[ DataRequired() ])
  close    = TimeField( label="close", format='%H:%M:%S',
                        render_kw={"step": "1"}, validators=[ DataRequired() ])

  list     = {
    "coffee" : ['✘','☕', '☕☕', '☕☕☕', '☕☕☕☕', '☕☕☕☕☕'],
    "wifi"   : ['✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'],
    "power"  : ['✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌']
  }
  
  coffee   = SelectField( label="coffee", choices = list["coffee"],
                          validators=[ DataRequired() ] )
  wifi     = SelectField( label="wifi", choices = list["wifi"], 
                           validators=[ DataRequired() ] )
  power    = SelectField( label="power", choices = list["power"], 
                           validators=[ DataRequired() ] )
  
  submit   = SubmitField( label= "Submit")

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods = [ "GET", "POST" ])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
        registration_data = {
        'name'     : form.name.data,
        'location' : form.location.data,
        'open'     : str(form.open.data),
        'close'    : str(form.close.data),
        'coffee'   : form.coffee.data,
        'wifi'     : form.wifi.data,
        'power'    : form.power.data
        }
        csv_data = [val for key,val in registration_data.items()]    
        with open('Day-62/cafe-data.csv',"a", newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(csv_data)
            return f'<h1> Registration Successfull </h1>\n{csv_data}'
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('Day-62/cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
