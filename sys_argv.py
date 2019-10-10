#!/usr/bin/python
####################################################################################################
# For examaple: ./sys_argv.py -t a -g b
####################################################################################################
import sys
print("sys.argv[0]: basename, sys.argv[1]: first parameter, sys.argv[2]: the second parameter, ...")
print("You can also treat as an array.")
print("sys.argv[0]: " + sys.argv[0] + ". The basename of the executable file.")
print("sys.argv[1]: " + sys.argv[1])
print("sys.argv[2]: " + sys.argv[2])
print("sys.argv[3]: " + sys.argv[3])
print("sys.argv[4]: " + sys.argv[4])
# print("sys.PS2: " + sys.PS2) # maybe useless

args = sys.argv[1:]
args.reverse()
print(' '.join(args))

