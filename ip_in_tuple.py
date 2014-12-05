__author__ = 'art'


import re

a = input()
pattern = re.compile(r"\.(\d+)")

b = pattern.findall(a)
c = tuple(b)
print(b)
print(c)