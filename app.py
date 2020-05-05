from flask import Flask, request, render_template, redirect, flash
from random import randint, choice, sample
# from flask_debugtoolbar import DebugToolbarExtension

# debug = DebugToolbarExtension(app)

app = Flask(__name__)

MOVIES = ["Avatar", "Avengers", "Schindler's List", "Gone with the Wind", "American History X"]

@app.route('/')
def home_page():
    """shows home page"""
    return render_template("home.html")

@app.route('/hello')
def index():
    """Shows hello page"""
    return render_template("hello.html")

@app.route('/movies')
def show_all_movies():
    return render_template('movies.html', movies=MOVIES)

@app.route('/movies/new', methods=["POST"])
def add_movie():
    title = request.form['title']
    # add to pretend DB
    MOVIES.append(title)
    flash('Created your movie!')
    flash('Good choice!')
    return redirect('/movies') # redirect to GET
    # if you do render_template again it will keep submitting the form


