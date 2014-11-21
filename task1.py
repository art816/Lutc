#!/usr/bin/env python3
#sfgsfgsgsfgf
#sdfsdf


import sys
import re
import unittest



def ip_host(ip_host_f):
    ''' соответствие ip и имени host'''
    line_number = 0

    #ippattern = re.compile(r'^(\d+.\d+.\d+.\d+)*(\b\w+)$')
    #ippattern = re.compile(r'^(\d+.\d+.\d+.\d+).*[\t|\ ](\w+[.\w]*)$')
    #ippattern = re.compile(r'^(\d+.\d+.\d+.\d+)([[\t|\ ].*[\t|\ ]]|[\t|\ ]) (\w+[\W\w+]*)$')

    ippattern = re.compile(r'^(\d+.\d+.\d+.\d+).*\s(\w+[\W\w+]*)$')
    res = {}
    with open(ip_host_f) as a_file:
        for a_line in a_file:
            line_number += 1
            a_rez = ippattern.match(a_line.rstrip())
            try:
                res[a_rez.groups()[1]] = a_rez.groups()[0]
            except AttributeError:  # Nothing found.
                pass
    return res

class TestHostLookup(unittest.TestCase):
    test_file_names = ['./data_test/t1.txt',
                       './data_test/t2.txt']
    expected_res = [{'localhost': '127.0.0.1'},
                    {'txt': '1.1.1.1'}]

    def test_basic(self):
        for test_fn, exp in zip(self.test_file_names, self.expected_res):
            res = ip_host(test_fn)
            assert res == exp, 'got:{} exp:{}'.format(res, exp)
    # a, b = b, a

def main():
    if len(sys.argv) == 1:
        unittest.main()
    elif len(sys.argv) == 2:
        ip_host(sys.argv[1])
    else:
        print('первый аргумент путь к фаилу')


if __name__ == '__main__':
    main()
