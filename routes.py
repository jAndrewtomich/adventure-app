from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/room1')
def room1():
    pass


@app.route('/room2')
def room2():
    pass