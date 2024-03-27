from flask import Flask

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper


app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1 style="text-align:center"> Hello </h1> '\
    '<iframe src="https://giphy.com/embed/8qCR6tGCytz05aXVwr" width="200"  frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/cat-tiger-bu2ma-8qCR6tGCytz05aXVwr"></a></p>'

@app.route('/<name>')
def greet(name):
    return f"Hello {name}!"

@app.route('/<name>/<int:number>')
def greet_(name,number):
    return f"Hello {name} and you are {number}"


@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye"



if __name__ == "__main__":
    app.run(debug=True)