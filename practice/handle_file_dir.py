#!/usr/bin/python3
# coding=utf-8
# -*- conding:utf-8 -*-

import os
file_path = './andywu.txt'
# os.unlink(file_path) # it is the same as below.
# os.remove(file_path)

try:
    os.remove(file_path)
except OSError as e:
    print("Error: %s : %s" %(file_path, e.strerror))





