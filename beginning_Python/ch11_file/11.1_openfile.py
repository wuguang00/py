#!/usr/bin/python
# coding=utf-8

f = open('somefile.txt', 'r+')
# f = open('somefile.txt', 'r+') # If the file doesn't exist, report error.
f.write('Hello, world 1.\n')
f.write('Hello, world 2.\n')

f.close()



