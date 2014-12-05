__author__ = 'art'

import psutil
import time
import unittest

import create_db as lite


class TestDB(unittest.TestCase):

    def test_basic(self):
        # data =('12.123.32.3', '345.3455,34545')
        # data = []
        # data.append(time.time())
        # data.append(psutil.cpu_times_percent())
        # data.append(psutil.swap_memory())
        # res = lite.create_db(data)
        # assert res, '{}'.format('не удалось записать в db')
        res = lite.look_db()
        assert res, '{}'.format('не удалось записать в db')


if __name__ == '__main__':
    unittest.main()