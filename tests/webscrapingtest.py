import unittest
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, 'src'))
from src import process
from bs4 import BeautifulSoup

class Test(unittest.TestCase):
    def test_get_soup(self):
        self.assertIsInstance(process.get_soup("https://github.com/"), BeautifulSoup)

if __name__ == '__main__':
    unittest.main()
