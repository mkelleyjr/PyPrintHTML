
# Michael L. Kelley Jr.
# March 3, 2018
# HTML.py
# Print the basic HTML structure of a web page
# Uses BeautifulSoup 4, lxml, requests, first do: 
# pip install bs4, pip install lxml, pip install requests


import requests
from bs4 import BeautifulSoup

# specifiy the page we want to grab HTML of 
page = requests.get("http://www.columbia.edu/~fdc/sample.html")

# parse the page 
soup = BeautifulSoup(page.content, "lxml")

# print the HTML out 
print (soup.prettify())