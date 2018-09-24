# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 23:14:31 2018

@author: enomu
"""

import artist_factory as fact

# mediator
class ArtistManager:
    def __init__(self, ax):
        self.artists = {}
        self.artist_factory = fact.ArtistFactory()

    def _search_by_id(self, artists, id):
        return [art for art in artists if art.get_id() == id]
        
    def _search_by_type(self, artists, type):
        return [art for art in artists if art.get_type() == type]
    
    def get_artist(self, id, type, marker=None):
        artists = self._search_by_type(self.artists, type)
        artists = self._search_by_id(artists, id)
    
        artist = artists[-1]    
        return artist
    