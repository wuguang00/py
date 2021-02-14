#!/usr/bin/python
# coding=utf-8

from random import choice

x = choice(['Hello, world', [1, 2, 'e', 'e', 4]])

print("The number of character 'e': {0}".format(x.count('e')))

print('abc'.count('a'))
print([1, 2, 'a', 'a', 'a'].count('a'))


print(1 + 2)
print("Fish" + "License")


