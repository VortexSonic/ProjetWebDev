import json
import requests
from flask import Flask, render_template
from pprint import pprint


app = Flask(__name__)

@app.route('/albums')
def albums():
    return render_template('html/albums.html')

@app.route('/artistes')
def artistes():
    return render_template('html/artistes.html')
    
@app.route('/clients')
def clients():
    return render_template('html/clients.html')

@app.route('/commandes')
def commandes():
    return render_template('html/commandes.html')

@app.route('/employes')
def employes():
    return render_template('html/employes.html')

@app.route('/genres')
def genres():
    return render_template('html/genres.html')

@app.route('/')
def index():
    return render_template('html/index.html')

@app.route('/infos')
def infos():
    return render_template('html/infos.html')

