
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('html/index.html')

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

@app.route('/infos')
def infos():
    return render_template('html/infos.html')

@app.route('/clients')
def clients():
    return render_template('html/clients.html')