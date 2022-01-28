from flask import render_template
from app import app


@app.route('/')
def fundament():
    return render_template('fundament.html')
