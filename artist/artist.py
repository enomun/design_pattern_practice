# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 21:13:36 2018

@author: enomun


"""

class ArtistBase(object):
    def __init__(self, artist_implement):
        self._artist_implement = artist_implement
        
    def update(self, **kw):
        self._artist_implement.update(**kw)

    def get_type(self):
        return self._artist_implement.get_type()

class ArtistWithTime(ArtistBase):
    def __init__(self, artist_implement, time, id):
        super(ArtistWithTime, self).__init__(artist_implement)
        self.time = time
        self.id = id
        
    def get_time(self):
        return self.time
    
    def get_id(self):
        return self.id
    
class ArtistWithState(ArtistBase):
    def __init__(self, artist_implement, time, id, duration=100):
        super(ArtistWithState, self).__init__(artist_implement)
        self.free_state = FreeState(self, time, duration)
        self.used_state = UsedState(self, time, duration)
        self.state = self.used_state

    def update(self, **kw):
        self._artist_implement.update(**kw)

    def update_time(self, time):
        self.state.update(time)

    def refresh(self, time):
        self.state.refresh(time)

    def can_use(self):
        return self.state.can_use()

# Base state
class State:
    def __init__(self, artist, time, duration):
        self.artist = artist
        self.time = time
        self.duration = duration #[ms]

# concrete state
class FreeState(State):
    def can_use(self):
        return True
    
    def update(self, time):
        self.artist.used_state.update(time)
        self.artist.state = self.artist.used_state
            
    def refresh(self, time):
        pass

class UsedState(State):
    def can_use(self):
        return False
    
    def update(self, time):
        self.time = time

    def refresh(self, time):
        if time - self.time > self.duration:
            self.artist.state = self.artist.free_state
            self.artist.update(visible=False)

            
if __name__ == "__main__":
    import artist_factory as fct
    import artist_implement as impl

    ax = []

    factory = fct.ScatterFactory()
    factory.set_artist(ArtistWithTime)
    art_time= factory.create_artist(ax, 19, id = "time")

    art_state=ArtistWithState(impl.Scatter(ax), time =0, id=1, duration=10)
    
    for t in range(40):
        art_state.refresh(t)
        print "time: %d, can_use:%s"%(t, art_state.can_use())
        
    
    
    
    