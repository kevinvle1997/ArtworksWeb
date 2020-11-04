import os
import sys
import unittest
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import db, Artist, Artwork, Museum

#some_engine = create_engine('postgresql+psycopg2://postgres:YOURPASSWORD@localhost/artworks')
#Session = sessionmaker(bind=some_engine)
#session = Session()


class Test(unittest.TestCase):
    '''
    def test_haveArtist_1(self):
        findartist = session.query(Artist).filter_by(artist_id = '6210').first()
        self.assertEqual(findartist.artist_id, '6210')
        
    def test_haveArtist_2(self):
        findartist = session.query(Artist).filter_by(artist_id = '7470').first()
        self.assertEqual(findartist.artist_name, 'Christian de Portzamparc')
        
    def test_haveArtwork_1(self):
        findartwork = session.query(Artwork).filter_by(artwork_id = '3343').first()
        self.assertEqual(findartwork.artwork_id, '00002')
        
    def test_haveArtwork_2(self):
        findartwork = session.query(Artwork).filter_by(artwork_id = '1992').first()
        self.assertEqual(findartwork.title, 'City of Music, National Superior Conservatory of Music and Dance, Paris, France, View from interior courtyard')
        
    def test_haveMuseum_1(self):
        findmuseum = session.query(Museum).filter_by(museum_id = '1').first()
        self.assertEqual(findmuseum.museum_id, '1')
        
    def test_haveMuseum_2(self):
        findmuseum = session.query(Museum).filter_by(museum_id = '2').first()
        self.assertEqual(findmuseum.museum_id, 'Tate Modern')
    '''
    # tests for Artist model
    #db.drop_all()
    def test_addArtist_1(self):
        newartist = Artist(artist_name='abc', artist_id='00001', gender='Male', artist_dates='01')
        db.session.add(newartist)
        db.session.commit()
        findartist = db.session.query(Artist).filter_by(artist_id='00001').first()
        self.assertEqual(findartist.artist_name, 'abc')
        db.session.delete(findartist)
        db.session.commit()
    
    def test_addArtist_2(self):
        newartist=Artist(artist_name='abcd',artist_id='00002')
        db.session.add(newartist)
        db.session.commit()
        findartist=db.session.query(Artist).filter_by(artist_id='00002').first()
        self.assertIsNone(findartist.gender)
        db.session.delete(findartist)
        db.session.commit()
        
    def test_addArtist_3(self):
        newartist=Artist(artist_name='abcde',artist_id='00003')
        db.session.add(newartist)
        db.session.commit()
        findartist=db.session.query(Artist).filter_by(artist_id='00003').first()
        db.session.delete(findartist)
        db.session.commit()
        findartist2=db.session.query(Artist).filter_by(artist_id='00003').first()
        self.assertIsNone(findartist2)
        
        
    #tests for Artwork model
    def test_addArtwork_1(self):
        newartwork = Artwork(title='def', artwork_id='00004')
        db.session.add(newartwork)
        db.session.commit()
        findartwork = db.session.query(Artwork).filter_by(artwork_id='00004').first()
        self.assertEqual(findartwork.title, 'def')
        db.session.delete(findartwork)
        db.session.commit()
    
    def test_addArtwork_2(self):
        newartwork = Artwork(title='defg', artwork_id='00005')
        db.session.add(newartwork)
        db.session.commit()
        findartwork = db.session.query(Artwork).filter_by(artwork_id='00005').first()
        self.assertIsNone(findartwork.date)
        db.session.delete(findartwork)
        db.session.commit()
        
    def test_addArtwork_3(self):
        newartwork = Artwork(title='defge', artwork_id='00006')
        db.session.add(newartwork)
        db.session.commit()
        findartwork = db.session.query(Artwork).filter_by(artwork_id='00006').first()
        db.session.delete(findartwork)
        db.session.commit()
        findartwork2 = db.session.query(Artwork).filter_by(artwork_id='00006').first()
        self.assertIsNone(findartwork2)

    #tests for Museum model
    def test_addMuseum_1(self):
        newmuseum = Museum(museum='ghi', museum_id='00007')
        db.session.add(newmuseum)
        db.session.commit()
        findmuseum = db.session.query(Museum).filter_by(museum_id='00007').first()
        self.assertEqual(findmuseum.museum, 'ghi')
        db.session.delete(findmuseum)
        db.session.commit()
    
    def test_addMuseum_2(self):
        newmuseum= Museum(museum='ghij')
        db.session.add(newmuseum)
        db.session.commit()
        findmuseum=db.session.query(Museum).filter_by(museum='ghij').first()
        self.assertIsNone(findmuseum.location)
        db.session.delete(findmuseum)
        db.session.commit()
        
    def test_addMuseum_3(self):
        newmuseum = Museum(museum='ghijk', museum_id='00008')
        db.session.add(newmuseum)
        db.session.commit()
        findmuseum = db.session.query(Museum).filter_by(museum_id='00008').first()
        db.session.delete(findmuseum)
        db.session.commit()
        findmuseum2 = db.session.query(Museum).filter_by(museum_id='00008').first()
        self.assertIsNone(findmuseum2)
    
    #tests for relationship
    def test_relationship_1(self):
        newartist=Artist(artist_name='someone', artist_id='00009')
        db.session.add(newartist)
        db.session.commit()
        newartwork=Artwork(title='defgh', artwork_id='00010',painter=newartist)
        db.session.add(newartwork)
        db.session.commit()
        findartwork=db.session.query(Artwork).filter_by(artwork_id='00010').first()
        self.assertEqual(findartwork.artist_id, '00009')
        db.session.delete(findartwork)
        db.session.commit()
        findartist=db.session.query(Artist).filter_by(artist_id='00009').first()
        db.session.delete(findartist)
        db.session.commit()
    
    def test_relationship_2(self):
        newmuseum=Museum(museum='ghijk', museum_id='00011')
        db.session.add(newmuseum)
        db.session.commit()
        newartwork=Artwork(title='defgh', artwork_id='00012',owner=newmuseum)
        db.session.add(newmuseum)
        db.session.commit()
        findartwork=db.session.query(Artwork).filter_by(artwork_id='00012').first()
        self.assertEqual(findartwork.artwork_id, '00012')
        db.session.delete(findartwork)
        db.session.commit()
        findmuseum=db.session.query(Museum).filter_by(museum_id='00011').first()
        db.session.delete(findmuseum)
        db.session.commit()
    
    

if __name__ == "__main__":
    unittest.main()
