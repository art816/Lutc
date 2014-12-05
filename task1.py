#!/usr/bin/env python3


import sys
import re
import unittest


def iphost(ip_host_f):
    ''' выделяем из строки ip и имя host '''
    line_number = 0
    iphost_ip_pattern = re.compile(r'^(\d+.\d+.\d+.\d+).*[\s\W]([\w.-]*)$')
    res = {}
    with open(ip_host_f) as a_file:
        for a_line in a_file:
            line_number += 1
            a_rez = iphost_ip_pattern.match(a_line.rstrip())
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
            res = iphost(test_fn)
            assert res == exp, 'got:{} exp:{}'.format(res, exp)


def main():
    if len(sys.argv) == 1:
        unittest.main()
    elif len(sys.argv) == 2:
        iphost(sys.argv[1])
    else:
        print('первый аргумент путь к фаилу')


if __name__ == '__main__':
    main()
