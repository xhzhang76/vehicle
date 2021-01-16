#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 16:14:07 2020

@author: pi
"""
import RPi.GPIO as GPIO
import time
import vehicle.Vehicle

PWMA = 18
AIN1 = 22
AIN2 = 27

PWMB = 23
BIN1 = 25
BIN2 = 24

class RaspberryWheelVehicle(vehicle.Vehicle):
    """
    mplement class
    """
    
    def __init__(self):
        """
        """
        pass

