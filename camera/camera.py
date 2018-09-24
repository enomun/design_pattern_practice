# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 22:14:43 2018

@author: enomun
"""


class Sensors:
    def __init__(self, pos, angles, params):
        self.pos
        self.angles        
        self.params
        
    def __str__(self):
        return "classname: %s, pos: %s, angles:%s"%(__name__, self.pos, self.angles)

    def get_pos(self):
        return self.pos

   
class Camera(Sensors):
    def __init__(self, pos, angles, params):
        self.pos = pos
        self.angles = angles
        self.params = params


    def capture(self):
        
        
        
#    def __str__(self):
#        return "pos: %s, angles:%s"%(self.pos, self.angles)



    
if __name__ == "__main__":
    from camera_builder_factory import CameraFactory
    
    params = {"position": [1,2,4],
              "angles": [15,40,0],
              "params": {"empty":[]}
              }
    
    factory = CameraFactory()
    camera = factory.create(params)
    
    