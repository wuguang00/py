#!/usr/bin/python
import fileinput
for line in fileinput.input():
    print(fileinput.isfirstline())
    print(line) # there is a enter in the result.
    print(fileinput.filename())
    print(fileinput.filelineno())
