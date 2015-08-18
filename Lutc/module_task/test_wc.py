__author__ = 'art'

import unittest
import random

import app.my_wc as my_wc

class TestApp(unittest.TestCase):
    """
    """
    @classmethod
    def setUpClass(cls):
        cls.file_name = 'test_file'
        cls.num_str = 1000
        cls.num_chars = 3
        cls.write_in(cls)

    def write_in(self):
        """
        """
        chars_for_line = self.num_chars // self.num_str
        ostatoc = self.num_chars % self.num_str
        with open(self.file_name, mode='w') as file:
            for num_str in range(self.num_str):
                data = ''
                for num_chars in range(chars_for_line):
                    data += chr(random.randint(ord('A'), ord('z')))
                if num_str == self.num_str - 1:
                    for num_dop_chars in range(ostatoc):
                        data += chr(random.randint(ord('A'), ord('z')))
                data += '\n'
                file.write(data)
    def test_coun_lines(self):
        """
        Set file name and assert number line
        """
        count_line = my_wc.count_lines(self.file_name)
        self.assertEqual(count_line, self.num_str)

    def test_coun_chars(self):
        """
        Set file name and assert number char
        """
        count_chars = my_wc.count_chars(self.file_name)
        self.assertEqual(count_chars, self.num_chars)

if __name__ == "__main__":
    unittest.main()