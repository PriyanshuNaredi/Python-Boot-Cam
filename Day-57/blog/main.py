from flask import Flask, render_template
import requests

response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
data = response.json()
    
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


if __name__ == "__main__":
    app.run(debug=True)
