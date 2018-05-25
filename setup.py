import os
import sys
from setuptools import setup

install_requires = ["requests", "pandas", "bs4"]
tests_require = ["bs4"]

base_dir = os.path.dirname(os.path.abspath(__file__))

version = "0.0.1"

setup(
    name = "GitHubWebScraping",
    version = version,
    description = "Web Scraping for Git Hub",
    long_description="\n\n".join([
        open(os.path.join(base_dir, "README.md"), "r").read()
    ]),
    url = "https://github.com/iran-gregorio/GitHubWebScraping",
    author = "Iran Gregorio",
    packages = ["src"],
    zip_safe = False,
    install_requires = install_requires,
    tests_require = tests_require,
    test_suite = "tests.get_tests",
)