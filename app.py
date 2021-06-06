# -*- coding: utf-8 -*-
from flask import Flask, render_template, jsonify
import json
import requests
from random import sample
from models import *

app = Flask(__name__)

@app.route('/')
def index():
    artistes = Artists.select().order_by(Artists.name)
    albums = Albums.select().order_by(Albums.title)
    genres = Genres.select().order_by(Genres.name)
    return render_template('index.html', artistes=artistes, albums=albums, genres=genres)


@app.route('/artistes')
def artistes():
    artistes = Artists.select().order_by(Artists.name)
    total = Artists.select().count()
    return render_template('artistes.html', artistes=artistes, total=total)

@app.route('/albums')
def albums():
    albums = Albums.select().order_by(Albums.title)
    total = Albums.select().count()
    return render_template('albums.html', albums=albums, total=total)

@app.route('/genres')
def genres():
    genres = Genres.select().order_by(Genres.name)
    total = Genres.select().count()
    return render_template('genres.html', genres=genres, total=total)


@app.route('/album/<id>/')
def album(id):
    albums = Albums.select().where(Albums.album_id == id)
    tracks = Tracks.select().where(Tracks.album == id)
    total = Tracks.select().where(Tracks.album == id).count()
    return render_template('album_details.html', albums=albums, tracks=tracks, total=total)

@app.route('/artiste/<id>/')
def artiste(id):
    artistes = Artists.select().where(Artists.artist_id == id)
    albums = Albums.select().where(Albums.artist == id)
    total = Albums.select().where(Albums.artist == id).count()
    return render_template('artiste_details.html', artistes=artistes, albums=albums, total=total)

@app.route('/genre/<id>/')
def genre(id):
    genres = Genres.select().where(Genres.genre_id == id)
    tracks = Tracks.select().where(Tracks.genre == id)
    total = Tracks.select().where(Tracks.genre == id).count()
    return render_template('genre_details.html', genres=genres, tracks=tracks, total=total)


@app.route('/clients')
def clients():
    clients = Customers.select().order_by(Customers.last_name)
    total = Customers.select().count()
    return render_template('clients.html', clients=clients, total=total)

@app.route('/production')
def production():
    return render_template('production.html')


@app.cli.command()
def initdb():
    """Create database"""
    create_tables()
    click.echo('Initialized the database')

@app.cli.command()
def dropdb():
    """Drop database tables"""
    drop_tables()
    click.echo('Dropped tables from database')