
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index/index.html')

@app.route('/artistes')
def artistes():
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
