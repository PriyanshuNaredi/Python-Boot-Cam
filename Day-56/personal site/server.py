from flask import Flask,render_template

app=Flask(__name__,template_folder='template',static_folder='static')
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(debug=True)