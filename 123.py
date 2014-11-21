__author__ = 'art'
import re
ipPattern = re.compile(r'(\W|\w+)*')
a_rez = ipPattern.search('12-3.sdf')
print(a_rez.group())
