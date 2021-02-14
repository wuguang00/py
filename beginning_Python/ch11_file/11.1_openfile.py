#!/usr/bin/python
# coding=utf-8

f = open('somefile.txt', 'w+')
# f = open('somefile.txt', 'r+') # If the file doesn't exist, report error.
f.write('Hello, world.')
f.close()

