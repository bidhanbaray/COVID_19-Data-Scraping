import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re
import xml.etree.ElementTree as ET

webPage = urllib.request.urlopen('https://iedcr.gov.bd/').read()
soupObject = BeautifulSoup(webPage,'html.parser')
tags = soupObject('td')

i = 0
while i<12:
    print(tags[i].contents[0],tags[i+3].contents[0])
    i+=4
