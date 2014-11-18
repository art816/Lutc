#!/usr/bin/env python3

import sys
import re
import unittest

def ip_host(ip_host_f):
    ''' соответствие ip и имени host'''
    line_number = 0
    #ipPattern = re.compile(r'^(\d+.\d+.\d+.\d+)*(\b\w+)$')
    #ipPattern = re.compile(r'^(\d+.\d+.\d+.\d+).*[\t|\ ](\w+[.\w]*)$')
    #ipPattern = re.compile(r'^(\d+.\d+.\d+.\d+)([[\t|\ ].*[\t|\ ]]|[\t|\ ])(\w+[\W\w+]*)$')
    ipPattern = re.compile(r'^(\d+.\d+.\d+.\d+).*[\t|\ ](\w+[\W\w+]*)$')
    res = {}
    with open(ip_host_f) as a_file:
        for a_line in a_file:
            line_number += 1
            a_rez = ipPattern.match(a_line.rstrip())
            #a_rez=ipPattern.search('1.2.3.4  \t\t\   gfdfgdfgs sfgsdf')
            try:
                res[a_rez.groups()[1]] = a_rez.groups()[0]
            except AttributeError:  # Nothing found.
                pass
    return res


class TestHostLookup(unittest.TestCase):
    test_file_name = './data_test/t1.txt'
    expected_basic = {'localhost': '127.0.0.1'}

    def test_basic(self):
        res = ip_host(self.test_file_name)
        assert res == self.expected_basic


def main():
    if len(sys.argv) == 1:
        unittest.main()
    elif len(sys.argv) == 2:
        ip_host(sys.argv[1])
    else:
        print('первый аргумент путь к фаилу')


if __name__ == '__main__':
    main()
