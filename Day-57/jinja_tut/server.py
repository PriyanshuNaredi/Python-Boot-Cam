from flask import Flask, redirect, url_for, render_template, request
import random
import datetime
import requests

app = Flask(__name__, template_folder='template')


@app.route('/', methods=['GET', 'POST'])
def home():
    random_num = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template('index.html', num=random_num, year=current_year)

@app.route("/guess/<name>")
def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data["gender"]
    
    age_url = f"https://api.agify.io?name={name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data["age"]
    return render_template("guess.html",p_name = name,p_gender = gender,p_age = age)

@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blog_url)
    all_post = response.json()
    return render_template('blog.html',posts = all_post)

if __name__ == '__main__':
    # DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000, debug=True)
