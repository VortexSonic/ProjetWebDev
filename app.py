
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index/index.html')

@app.route('/artistes')
def index():
    return render_template('artistes/artistes.html')

@app.route('/albums')
def index():
    return render_template('albums/albums.html')

@app.route('/employes')
def index():
    return render_template('employes/employes.html')

@app.route('/genres')
def index():
    return render_template('genres/genres.html')