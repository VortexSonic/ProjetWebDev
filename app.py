import json

from flask import Flask, render_template
from pprint import pprint


app = Flask(__name__)

@app.route('/albums')
def albums():
    return render_template('albums.html')

@app.route('/artistes')
def artistes():
    return render_template('artistes.html')
    
@app.route('/clients')
def clients():
    return render_template('clients.html')

@app.route('/commandes')
def commandes():
    return render_template('commandes.html')

@app.route('/employes')
def employes():
    return render_template('employes.html')

@app.route('/genres')
def genres():
    return render_template('genres.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/infos')
def infos():
    return render_template('infos.html')

