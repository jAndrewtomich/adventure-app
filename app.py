import os
from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run()

#This is meant to be a game modeled after a choose-your-own adventure book.
