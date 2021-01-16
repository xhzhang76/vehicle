#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 16:14:07 2020

@author: pi
"""

import RPi.GPIO as GPIO
import time
from vehicle import Vehicle

PWMA = 18
AIN1 = 22
AIN2 = 27
PWMB = 23
BIN1 = 25
BIN2 = 24


class RaspberryWheelVehicle(Vehicle):
    """
    implement class
    """

    def __init__(self, t_time):
        """
        """
        super().__init__()
        self.__time = t_time
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(AIN2, GPIO.OUT)
        GPIO.setup(AIN1, GPIO.OUT)
        GPIO.setup(PWMA, GPIO.OUT)
        GPIO.setup(BIN1, GPIO.OUT)
        GPIO.setup(BIN2, GPIO.OUT)
        GPIO.setup(PWMB, GPIO.OUT)

        self.__left_motor = GPIO.PWM(PWMA, 100)
        self.__left_motor.start(0)

        self.__right_motor = GPIO.PWM(PWMB, 100)
        self.__right_motor.start(0)

    def forward(self, speed):
        super().forward(speed)
        self.__left_motor.ChangeDutyCycle(speed)
        GPIO.output(AIN2, False)  # AIN2
        GPIO.output(AIN1, True)  # AIN1

        self.__right_motor.ChangeDutyCycle(speed)
        GPIO.output(BIN2, False)  # BIN2
        GPIO.output(BIN1, True)  # BIN1
        time.sleep(self.__time)

    def backward(self, speed):
        self.__left_motor.ChangeDutyCycle(speed)
        GPIO.output(AIN2, True)  # AIN2
        GPIO.output(AIN1, False)  # AIN1

        self.__right_motor.ChangeDutyCycle(speed)
        GPIO.output(BIN2, True)  # BIN2
        GPIO.output(BIN1, False)  # BIN1
        time.sleep(self.__time)

    def left(self, speed):
        super().left(speed)

    def right(self, speed):
        super().right(speed)


if __name__ == '__main__':
    vehicle = RaspberryWheelVehicle(3)
    vehicle.backward(60)
    vehicle.forward(50)
