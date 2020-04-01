#!/usr/bin/python
# a method to traversal directories.
import os
print("The first turn, topdown is False")
for root, dirs, files in os.walk("/Users/wuguang/practice", topdown=False):
    print("\noverall")
    print(root, dirs, files)
    print("\nfile")
    for name in files:
        print(os.path.join(root, name))
    print("\n\n\ndir")
    for name in dirs:
        print(os.path.join(root, name))

print("\n\n\n\nThe second turn, topdown is True")
for root, dirs, files in os.walk("/Users/wuguang/practice", topdown=True):
    print("\noverall")
    print(root, dirs, files)
    print("\nfile")
    for name in files:
        print(os.path.join(root, name))
    print("\n\n\ndir")
    for directory in dirs:
        print(os.path.join(root, directory))


