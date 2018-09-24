# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 22:39:22 2018

@author: enomu
"""

import artist as art
import artist_implement as impl


# abstract
class ArtistFactory:
    def __init__(self):
        self.Artist = art.ArtistWithTime
    
    def set_artist(self, Artist):
        self.Artist = Artist

# concrete
class ScatterFactory(ArtistFactory):  
    def create_artist(self, ax, time, id):
        artist = self.Artist(impl.Scatter(ax), time, id)
        return artist
    
    
    
if __name__ == "__main__":
    factory = ScatterFactory()
    ax = []
    artist1 = factory.create_artist(ax, 19, id="a")

    factory.set_artist(art.ArtistWithState)
    art2 = factory.create_artist(ax, 19, id="state")
    