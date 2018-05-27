# GitHubWebScraping 

[![Build Status](https://travis-ci.org/iran-gregorio/GitHubWebScraping.svg?branch=master)](https://travis-ci.org/iran-gregorio/GitHubWebScraping) [![Coverage Status](https://coveralls.io/repos/github/iran-gregorio/GitHubWebScraping/badge.svg?branch=master&service=github)](https://coveralls.io/github/iran-gregorio/GitHubWebScraping?branch=master&service=github)

Web Scraping com Python no GitHub

1. Install modules in requirements.txt
2. Execute src\process.py with parameters:
  - -fi = File input repositores.txt
  - -do = Directory output to result files
  
  ``` sh
  $ python src\process.py -fi=[FILE INPUT] -do=[OUTPUT DIRECTORY]
  ```
  
  To run tests:
  
  ```sh
  $ python setup.py test
  ```
