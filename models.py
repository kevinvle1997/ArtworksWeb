from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import (assert_nullable,assert_non_nullable, assert_max_length)
from sqlalchemy.orm import sessionmaker
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_STRING",'postgres://postgres:YOURPASSWORD@localhost:5432/artworks')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # to suppress a warning message
db = SQLAlchemy(app)


#defines artists
class Artist(db.Model):
    """
    The artist calss defines the artist table which contains all of the artists for this project
    artist_name is the name of the artist
    gender is the listd gender of the artist
    nationality is the country of origin for the artist
    artist_id is a unique idetifier for the artist created by us
    This table contains one forign relation:
    Artworks is a relationship to the artworks table that lets us view the art work for that artist
    """
    __tablename__ = 'artist'

    artist_name = db.Column(db.String(), nullable=True)
    gender = db.Column(db.String(), nullable=True)
    artist_dates = db.Column(db.String(), nullable=True)
    nationality = db.Column(db.String(), nullable=True)
    artist_id = db.Column(db.String(), primary_key=True)

    artworks = db.relationship('Artwork', backref='painter')

#defines artwork
class Artwork(db.Model):
    """
    The Artwork class defined the artwork table which contains all artwork for this project.
    artist is the name of the artist
    date is the date of the peice was created
    medium is the type of material used to make the art 
    credit is acknowledgement of the artwork's donor
    acquired_date is the date the museum obtained the art
    imageURL links to the image of the art - not all pieces have this
    dimensions lists the size of the piece
    museum is where the art is located
    title is the artworks name
    artwork_id is a primary key created by us to identify each artwork
    contains two forign keys:
    artist_id which links to the artist table
    museum_id which links to the museum table
    """
    __tablename__ = 'artwork'

    artist = db.Column(db.String(), nullable=True)
    date = db.Column(db.String(), nullable=True)
    medium = db.Column(db.String(), nullable=True)
    credit = db.Column(db.String(), nullable=True)
    acquired_date = db.Column(db.String(), nullable=True)
    imageURL = db.Column(db.String(), nullable=True)
    dimensions = db.Column(db.String(), nullable=True)
    museum = db.Column(db.String(), nullable=True)
    title = db.Column(db.String(), nullable =True)
    artwork_id = db.Column(db.String(), primary_key=True)

    artist_id = db.Column(db.String(), db.ForeignKey('artist.artist_id'))
    museum_id = db.Column(db.Integer, db.ForeignKey('museum.museum_id'))

#Defines museums
class Museum(db.Model):
    """
    The museum class defines the model for museum in the artworks database. There are three attributes museum, location, and museum_id.
    Museum is the name of the museum. 
    Location descibes the city and country where the museum is located.
    Museum_id is the primary key for this relation.
    contains a relationship to artwork
    """
    __tablename__ = 'museum'

    museum = db.Column(db.String(), nullable=True)
    location = db.Column(db.String(), nullable=True)
    museum_id = db.Column(db.Integer, primary_key=True)

    artworks = db.relationship('Artwork', backref='owner')



db.drop_all()
db.create_all()

#assertion checking
artist = Artist(artist_name='John', gender='Male', nationality='US', artist_id='00001')
db.session.add(artist)
db.session.commit()
artwork=Artwork(artist='Emily', museum='Moma', title='masterpiece', artwork_id='00002')
db.session.add(artwork)
db.session.commit()
museum=Museum(museum='moma', location='France', museum_id='00003')
db.session.add(museum)
db.session.commit()

assert_nullable(artist, 'artist_name')
assert_nullable(artist, 'gender')
assert_nullable(artist, 'nationality')
assert_nullable(artwork, 'artist')
assert_nullable(artwork, 'museum')
assert_nullable(artwork, 'title')
assert_nullable(museum, 'museum')
assert_nullable(museum, 'location')

db.session.query(Artist).delete()
db.session.commit()
db.session.query(Artwork).delete()
db.session.commit()
db.session.query(Museum).delete()
db.session.commit()
# End of models.py




