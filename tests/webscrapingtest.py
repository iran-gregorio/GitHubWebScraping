import unittest
import os
import sys
import requests

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, 'src'))
from src import process
from src.element import Element
from bs4 import BeautifulSoup

class Test(unittest.TestCase):
    def test_get_soup(self):
        self.assertIsInstance(process.get_soup("https://github.com/"), BeautifulSoup)

    def test_get_file_info(self):
        soup = process.get_soup("https://github.com/iran-gregorio/GitHubWebScraping/blob/master/README.md")
        element = Element("", "", 0)
        process.get_fileInfo(soup, element)
        self.assertGreater(element.lines, 0)
        self.assertGreater(element.size, 0)

    def test_get_element_list(self):
        soup = process.get_soup("https://github.com/iran-gregorio/GitHubWebScraping")
        elementList = process.get_elementList(soup, 0)
        self.assertGreater(len(elementList), 0)

    def test_multi_run_process(self):
        process.multi_run_process(("iran-gregorio/GitHubWebScraping", "./Result/"))
        self.assertTrue(True)

    def test_get_full_path_file_raises_exception(self):
        self.assertRaises(FileNotFoundError, process.get_full_path, "./repositores.txt", True)
    
    def test_get_full_path_directory(self):
        self.assertTrue(os.path.abspath(process.get_full_path("Result", False)))

if __name__ == '__main__':
    unittest.main()
