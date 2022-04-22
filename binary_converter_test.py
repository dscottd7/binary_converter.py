# Author: D. Scott DiPerna
# GitHub username: dscottd7
# Date: 4/21/2022
# Description: unit tests for recursive_binary_function

import unittest
from binary_converter import recursive_binary_function

class TestRecursiveConverter(unittest.TestCase):
    def test0(self):
        integer = 3
        string = ""
        bin_str = recursive_binary_function(integer, string)
        self.assertEqual(bin_str, "0011")

    def test1(self):
        integer = 13
        string = ""
        bin_str = recursive_binary_function(integer, string)
        self.assertEqual(bin_str,"00001101")

    def test2(self):
        integer = 139
        string = ""
        bin_str = recursive_binary_function(integer, string)
        self.assertEqual(bin_str,"000010001011")

if __name__ == '__main__':
  unittest.main()
