#!/usr/bin/python3
# coding=utf-8
# -*- conding:utf-8 -*-
print("Hello, world")

import math
print(math.sin(1))

import sys
sys.path.append('~/database/py')
import hello
import hello # only one time, this will not input to namespace again
hello

import importlib # this is new features
hello=importlib.reload(hello)
hello=importlib.reload(hello) # reload again

import sys, pprint
pprint.pprint(sys.path)

