
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index/index.html')

@app.route('/artistes')
def artistes():
    return render_template('index/artistes.html')