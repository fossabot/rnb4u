#!/usr/bin/python
import requests
from bs4 import BeautifulSoup

# import urllib2
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

url = "https://rnb4u.in/"

data  = urlopen(url)
soup = BeautifulSoup(data, "lxml")

with open('music.txt', 'w') as f:
    for i in soup.find_all('a', attrs={'class':'sm2_link'}):

        music = []
        m = i.text
        music.append(m)

        f.write("https://rnb4u.in/upload/music/" + "{0}".format("\n".join(music)) + ".mp3" "\n")
