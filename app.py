
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index/index.html')

@app.route('/artistes')
def artistes():
<<<<<<< HEAD
    return render_template('index/artistes.html')
=======
    return render_template('html/artistes.html')

@app.route('/albums')
def albums():
    return render_template('html/albums.html')

@app.route('/employes')
def employes():
    return render_template('html/employes.html')

@app.route('/genres')
def genres():
    return render_template('html/genres.html')
>>>>>>> 82ecd7d0c2a2d264ae6c0713aab7fa7d9648d9fe
