#!/usr/bin/python
# coding=utf-8
# this script used ConfigParser, but the module is only used in python2.x
import ConfigParser
import re

config = ConfigParser.ConfigParser() # instance a class
config.read("iruntool.core")         # read a file
CORELOAD_RE = re.compile(r"\/?(?P<core>(\w)+)\.core") # regular expression to distinguish the target string.

# \/? is used for / has 0 or 1, has or not has is OK
# ?P<core> is a special case, matched items put into a group named core.
m = CORELOAD_RE.match(r"iruntool.core")
print(m.group())                     # match the whole file name.
print(m.group('core'))               # iruntool is matched

print('''

      use re like this:
      if re.search(pat, string):
          print("Found.")
          match used as the start of a string.
          search used in the string is OK for the whole string.

      ''')

if re.match('P', 'Python'):
    print('OK, matched a "P" at the start of this line.')

if re.match('P', 'jPython'):
    print('OK, matched a "P" at the start of this line.')
else:
    print('Oh, not matched a "P"')

if re.search('P', 'jPython'):
    print('OK, matched a "P" in this string.')
else:
    print('Oh, not matched a "P"')

p = re.compile(r'(?P<word>\s\s\b\w+\b)') # \s matchs unicode str with empty show ^ \t\r\n\f\v \S is correspond it.
m = p.search(r'((( Lots of punctuation  dd)))') # \b empty string.
print(m.group())                         # I just want to make what can be done through this command.
print(m.group('word'))

q = re.compile(r'(?:\w+)')               # don't record the group.
n = q.search('(((( Lots of punctuation )))') # an object
print(n.group())

sentence = 'cats are fast'
regexp = re.compile('(?P<animal>\w+) (?P<verb>\w+) (?P<adjective>\w+)') # just assigned a rule for it now. must have matched item, so you can call groupdict()
matched = re.search(regexp, sentence)
print(matched.group())
print(matched.groupdict())

some_text = 'alpha, beta, gama, delta, wuguang'
m = re.split(', ', some_text)
print(m)

print(re.split('o(o)', 'foobar'))
print(re.split('oooo(b)', 'foooobar'))
print(re.split('oo(oo)', 'foooobar'))
print(re.escape('www.python.org'))
print(re.escape('www python org')) # show the ecape characters should be added.





