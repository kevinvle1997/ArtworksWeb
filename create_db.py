# beginning of create_db.py
import json
import requests
import itertools
from collections import OrderedDict
from flask import Flask, render_template, json
import csv, gitlab
import pandas as pd
from models import app, db, Artist, Artwork, Museum  

def load_data(dataUrl):
    dataHolder={}
    for name,url in dataUrl.items():
        df = pd.read_csv(url[0], error_bad_lines=False, nrows =url[1] , skiprows = url[2]).T.to_dict()
        dataHolder[name] = df
    return dataHolder

def create_museums_db():

    #load museum data
    with open('museum.json') as f:
        museums = json.load(f)
        #processes muesum data
        for dmuseum in museums['museum']:
            museum_id = dmuseum["museum_id"]
            museum = dmuseum["museum"]
            location = dmuseum["location"]

            #process moma data
            if museum == "Museum of Modern Art":
                moma = Museum(museum = museum, location = location, museum_id=museum_id)
                db.session.add(moma)
                db.session.commit()
            #process Tate data
            elif museum == "Tate Modern":
                tate = Museum(museum = museum, location = location, museum_id=museum_id)
                db.session.add(tate)
                db.session.commit()
        f.close()
    
    # load artist data
    artistfiles = {"momaArtist":["moma_artists.csv",250,None],\
    "tateArtist":["tate_artist_data.csv",100,None]}
    artistData = load_data(artistfiles)
    
    #processes artist data
    for museumName, museumData in artistData.items():
        for index in museumData:
       
            if museumName == "momaArtist":
                gender = museumData[index]["Gender"]
                artist_id = str(museumData[index]["ConstituentID"]) + "_moma"
                artist_name = museumData[index]["DisplayName"]
                artist_dates = museumData[index]["BeginDate"]
                nationality = museumData[index]["Nationality"]
            elif museumName == "tateArtist":
                gender = museumData[index]["gender"]
                artist_id = str(museumData[index]["id"]) + "_tate"
                artist_name = museumData[index]["name"]
                artist_dates = museumData[index]["dates"]
                nationality = museumData[index]["placeOfBirth"]

            newArtist = Artist(artist_id = artist_id, artist_name = artist_name, artist_dates = artist_dates, gender=gender, nationality = nationality)
            db.session.add(newArtist)
            db.session.commit()

    # load artwork data
    artworkfiles = {"momaArtwork":['moma_artworks.csv',750, None],\
    "tateArtwork":["tate_artwork_data.csv",400,None]}
    artworkData = load_data(artworkfiles)

    #proceses artwork data
    for museumName, museumData in artworkData.items():

        for index in museumData:
            
            #processes moma data
            if museumName == "momaArtwork":
                # skips columens with an artist ID error
                if "," in str(museumData[index]["ConstituentID"]) :
                    pass
                else:
                    title = museumData[index]["Title"]
                    artist = museumData[index]["Artist"]
                    artist_id = str(museumData[index]["ConstituentID"]) + "_moma"
                    date = museumData[index]["Date"]
                    medium = museumData[index]["Medium"]
                    credit = museumData[index]["CreditLine"]
                    acquired_date = museumData[index]["DateAcquired"] 
                    imageURL = museumData[index]["ThumbnailURL"]
                    dimensions = museumData[index]["Dimensions"]
                    artwork_id = str(museumData[index]["ObjectID"]) + "_moma"

                    newArtwork = Artwork(title = title, artist = artist, artist_id= artist_id, date = date, \
                        medium = medium,  credit = credit, acquired_date = acquired_date, imageURL = imageURL, \
                    dimensions = dimensions, artwork_id = artwork_id, owner = moma)

            #processes tate data 
            elif museumName == "tateArtwork":
                title = museumData[index]["title"]
                artist = museumData[index]["artist"]
                artist_id = str(museumData[index]["artistId"]) + "_tate"
                date = museumData[index]["year"]
                medium = museumData[index]["medium"]
                credit = museumData[index]["creditLine"]
                acquired_date = museumData[index]["acquisitionYear"]
                imageURL = museumData[index]["thumbnailUrl"]
                dimensions = museumData[index]["dimensions"]
                artwork_id = str(museumData[index]["id"]) + "_tate"

                newArtwork = Artwork(title = title, artist = artist, artist_id= artist_id, date = date, \
                    medium = medium,  credit = credit, acquired_date = acquired_date, imageURL = imageURL, \
                    dimensions = dimensions, artwork_id = artwork_id, owner = tate)

            db.session.add(newArtwork)
            db.session.commit()
create_museums_db()
# end of create_db.py