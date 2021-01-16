#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 23:23:23 2020

@author: xhzhang76
"""


class Vehicle(object):
    """
         Definition of vehile interface
         Physical parameter, actions and etc
    """
    
    def __init__(self):
        """
            Init vehicle parameters, include: 
            width/height/long etc.
        """
        pass
    
    def forward(self, speed):
        pass
    
    def backward(self, speed):
        pass
    
    def left(self, speed):
        pass
    
    def right(self, speed):
        pass
    
    def stop(self):
        pass