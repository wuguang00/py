#!/usr/bin/python3
# coding=utf-8
# -*- conding:utf-8 -*-

# this file can't be executed.
from turtle import *
from random import randint
from colorsys import hsv_to_rgb

step=30                # length of each step
nsteps=2000             # number of steps
hinc=1.0/nsteps        # hue increment
width(2)               # width of line

(w,h) = screensize()   # boundaries of walk
speed('fastest')
colormode(1.0)         # clours 0:1 instead of 0:255
bgcolor('black')       # black background
hue = 0.0
for i in range(nsteps):
    setheading(randint(0,359))
    # https//docs.python.org/2/library/colorsys.html
    color(hsv_to_rgb(hue, 1.0, 1.0)) # pen color in RGB
    hue+=hinc                        # change color
    forward(step)                    # step along
    (x,y)=pos()
    if abs(x) > w or abs(y) > h:
        backward(step)

done()

