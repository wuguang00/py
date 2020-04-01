#!/usr/bin/python3
# coding=utf-8
# -*- conding:utf-8 -*-
class class1():
    def a1():
        return "hello"
# below properties are reserved
print(class1.__doc__)
print(class1.__name__)
print(class1.__module__)
print(class1.__bases__)
print(class1.__dict__)
print(class1.__class__)
x = class1()

print(repr(x))
print(str(x))
# print(bytes(x)) # used in python3

