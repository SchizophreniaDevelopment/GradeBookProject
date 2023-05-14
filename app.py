from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/welcome_get.php')
def welcome():
    return render_template("welcome_get.php")