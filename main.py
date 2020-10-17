import itertools
from collections import OrderedDict
from flask import Flask, render_template, json, request, redirect, url_for
import csv, gitlab
import pandas as pd
from create_db import app, db, Artist, Artwork, Museum, create_museums_db



#json dump for artist
@app.route('/artist/JSON')
def artistJSON():
    r = json.dumps(artists)
    return r

#json dump for artwork
@app.route('/artwork/JSON')
def artworkJSON():
    r = json.dumps(artworks)
    return r

#renders home page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        userInput = request.form['data']
        ArtistD = db.session.query(Artist).filter(Artist.artist_name.ilike("%"+userInput+ "%")).all()
        ArtworkD = db.session.query(Artwork).filter(Artwork.title.ilike("%"+userInput+ "%")).all()
        MuseumD = db.session.query(Museum).filter(Museum.museum.ilike("%"+userInput+ "%")).all()
        global results
        results = {'artist': ArtistD, 'artwork': ArtworkD, 'museum': MuseumD}
        return redirect(url_for("search"))
    else:
        return render_template('index.html')

#renders about page
@app.route('/about/', methods=['GET', 'POST'])
def about():
    # for searching function
    if request.method == 'POST':
        userInput = request.form['data']
        ArtistD = db.session.query(Artist).filter(Artist.artist_name.ilike("%"+userInput+ "%")).all()
        ArtworkD = db.session.query(Artwork).filter(Artwork.title.ilike("%"+userInput+ "%")).all()
        MuseumD = db.session.query(Museum).filter(Museum.museum.ilike("%"+userInput+ "%")).all()
        global results
        results = {'artist': ArtistD, 'artwork': ArtworkD, 'museum': MuseumD}
        return redirect(url_for("search"))
    else:
        return render_template('about.html')

#renders artists page
@app.route('/artist/', methods=['GET', 'POST'])
def artist():
    # for searching function
    if request.method == 'POST':
        userInput = request.form['data']
        ArtistD = db.session.query(Artist).filter(Artist.artist_name.ilike("%"+userInput+ "%")).all()
        ArtworkD = db.session.query(Artwork).filter(Artwork.title.ilike("%"+userInput+ "%")).all()
        MuseumD = db.session.query(Museum).filter(Museum.museum.ilike("%"+userInput+ "%")).all()
        global results
        results = {'artist': ArtistD, 'artwork': ArtworkD, 'museum': MuseumD}
        return redirect(url_for("search"))
    artists = db.session.query(Artist).all()
    return render_template('artist.html', artists=artists)

#renders arworks page
@app.route('/artwork/', methods=['GET', 'POST'])
def artwork():
    # for searching function
    if request.method == 'POST':
        userInput = request.form['data']
        ArtistD = db.session.query(Artist).filter(Artist.artist_name.ilike("%"+userInput+ "%")).all()
        ArtworkD = db.session.query(Artwork).filter(Artwork.title.ilike("%"+userInput+ "%")).all()
        MuseumD = db.session.query(Museum).filter(Museum.museum.ilike("%"+userInput+ "%")).all()
        global results
        results = {'artist': ArtistD, 'artwork': ArtworkD, 'museum': MuseumD}
        return redirect(url_for("search"))
    artworks = db.session.query(Artwork).all()
    return render_template('artwork.html', artworks=artworks)

#renders museums 
@app.route('/museum/', methods=['GET', 'POST'])
def museum():
    # for searching function
    if request.method == 'POST':
        userInput = request.form['data']
        ArtistD = db.session.query(Artist).filter(Artist.artist_name.ilike("%"+userInput+ "%")).all()
        ArtworkD = db.session.query(Artwork).filter(Artwork.title.ilike("%"+userInput+ "%")).all()
        MuseumD = db.session.query(Museum).filter(Museum.museum.ilike("%"+userInput+ "%")).all()
        global results
        results = {'artist': ArtistD, 'artwork': ArtworkD, 'museum': MuseumD}
        return redirect(url_for("search"))
    museums = db.session.query(Museum).all()
    return render_template('museum.html', museums = museums)

#renders individual artist page
@app.route('/artist/<string:artist_id>/view/', methods=['GET','POST'])
def view_artist(artist_id):
    # for searching function
    if request.method == 'POST':
        userInput = request.form['data']
        ArtistD = db.session.query(Artist).filter(Artist.artist_name.ilike("%"+userInput+ "%")).all()
        ArtworkD = db.session.query(Artwork).filter(Artwork.title.ilike("%"+userInput+ "%")).all()
        MuseumD = db.session.query(Museum).filter(Museum.museum.ilike("%"+userInput+ "%")).all()
        global results
        results = {'artist': ArtistD, 'artwork': ArtworkD, 'museum': MuseumD}
        return redirect(url_for("search"))
    specific_artist = db.session.query(Artist).get(artist_id)
    artwork = db.session.query(Artwork).filter(Artwork.artist_id == artist_id)
    return render_template("view_artist.html", specific_artist = specific_artist, artwork = artwork)

#renders individual artwork page
@app.route('/artwork/<string:artwork_id>/view/', methods=['GET','POST'])
def view_artwork(artwork_id):
    # for searching function
    if request.method == 'POST':
        userInput = request.form['data']
        ArtistD = db.session.query(Artist).filter(Artist.artist_name.ilike("%"+userInput+ "%")).all()
        ArtworkD = db.session.query(Artwork).filter(Artwork.title.ilike("%"+userInput+ "%")).all()
        MuseumD = db.session.query(Museum).filter(Museum.museum.ilike("%"+userInput+ "%")).all()
        global results
        results = {'artist': ArtistD, 'artwork': ArtworkD, 'museum': MuseumD}
        return redirect(url_for("search"))
    specific_artwork = db.session.query(Artwork).get(artwork_id)
    return render_template("view_artwork.html", dictionary = specific_artwork)

#renders individual museum page
@app.route('/museum/<int:museum_id>/view/', methods=['GET','POST'])
def view_museum(museum_id):
    # for searching function
    if request.method == 'POST':
        userInput = request.form['data']
        ArtistD = db.session.query(Artist).filter(Artist.artist_name.ilike("%"+userInput+ "%")).all()
        ArtworkD = db.session.query(Artwork).filter(Artwork.title.ilike("%"+userInput+ "%")).all()
        MuseumD = db.session.query(Museum).filter(Museum.museum.ilike("%"+userInput+ "%")).all()
        global results
        results = {'artist': ArtistD, 'artwork': ArtworkD, 'museum': MuseumD}
        return redirect(url_for("search"))
    specific_museum = db.session.query(Museum).get(museum_id)
    return render_template("view_museum.html", dictionary = specific_museum)

#renders arworks page
@app.route('/unit/', methods=['GET', 'POST'])
def unit():
    return render_template('testCases.html')

#renders arworks page
@app.route('/search/', methods=['GET', 'POST'])
def search():
    # for searching function
    if request.method == 'POST':
        userInput = request.form['data']
        ArtistD = db.session.query(Artist).filter(Artist.artist_name.ilike("%"+userInput+ "%")).all()
        ArtworkD = db.session.query(Artwork).filter(Artwork.title.ilike("%"+userInput+ "%")).all()
        MuseumD = db.session.query(Museum).filter(Museum.museum.ilike("%"+userInput+ "%")).all()
        global results
        results = {'artist': ArtistD, 'artwork': ArtworkD, 'museum': MuseumD}
        return redirect(url_for("search"))
    holder = results
    return render_template('search.html', resultsD = holder)

if __name__ == '__main__':
    app.run()
