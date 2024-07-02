from flask import render_template
from app import app

@app.route('/')
def home():
   return "<b>Mi segundo Docker</b>"

@app.route('/home')
def home_2():
   return render_template('home.html')
