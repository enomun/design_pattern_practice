# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 21:15:54 2018

@author: enomu
"""

import numpy as np
from camera import Camera

class CameraDirector:      
    def extract_params(self, params):
        pos = params["position"]
        angles = params["angles"]
        camera_params = params["params"]
        return pos, angles, camera_params

    def construct_sensor(self, builder, params):
        pos, angles, camera_params = self.extract_params(params)

        builder.add_global_pos(pos)
        builder.add_euler_angles(angles)
        builder.add_id(1)
        builder.add_frequency(10)    
        builder.add_params(camera_params)
        return builder.get_sensor()    
    
class CameraBuilder:
    def add_global_pos(self, pos):
        self._pos = np.array(pos)

    def add_euler_angles(self, angles):
        self._angles = np.array(angles)

    def add_params(self, params):
        self._camera_params = params
        
    def add_id(self, id):
        self._id = id

    def add_frequency(self, freq):
        self._freq = freq
        
    def get_sensor(self):
        return Camera(self._pos, self._angles, self._camera_params)

class CameraFactory:
    def extract_params(self, params):
        pos = np.array(params["position"])
        angles = np.array(params["angles"])
        camera_params = params["params"]
        return pos, angles, camera_params
    
    def create(self, params):
        pos, angles, camera_params = self.extract_params(params)
        return Camera(pos, angles, camera_params)

if __name__ == "__main__":
    
    params = {"position": [1,2,4],
              "angles": [15,40,0],
              "params": {"empty":[]}
              }

    # director pattern
    camera_director = CameraDirector()
    camera_builder = CameraBuilder()
    cam = camera_director.construct_sensor(camera_builder, params)    
    print cam

    # abstract factory pattern
    factory = CameraFactory()
    cam2 = factory.create(params)
    print cam2
    
    # factory patern
    creator = CameraFactory()
    cam3 = creator.create(params)
    
    print cam3