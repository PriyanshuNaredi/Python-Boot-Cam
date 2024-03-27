from flask import Flask, render_template
import requests


# response = requests.get('https://api.npoint.io/4cedc647e52fc72c2543')
response = requests.get('https://gist.githubusercontent.com/gellowg/389b1e4d6ff8effac71badff67e4d388/raw/fc31e41f8e1a6b713eafb9859f3f7e335939d518/data.json')
data = response.json()
print(type(data[0]))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html",data = data)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in data:
        if blog_post["id"] == index:
            curr_id = index - 1
            print(data[curr_id]["title"])
    return render_template("post.html",post=data, curr_id=curr_id)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")



if __name__ == "__main__":
    app.run(debug=True)
