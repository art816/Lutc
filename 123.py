__author__ = 'art'
import re
ipPattern = re.compile(r'(\(.*\))')
a_rez = ipPattern.search('(er, f, ,f gserg).sdf')
print(a_rez.group())
