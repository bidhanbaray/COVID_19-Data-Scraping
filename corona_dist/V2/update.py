#reading pdf from online
import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup

website = "https://iedcr.gov.bd/"
print('Requesting Access to',website,'... ...')
webPage = urllib.request.urlopen(website).read()
soupObject = BeautifulSoup(webPage,'html.parser')
anchorTags = soupObject('a')
url = anchorTags[0].get('href',None)
link2 = website+url
print('Updating... ... Please wait...')

file = open('data_update.pdf','wb')
handle = urllib.request.urlopen(link2).read()
file.write(handle)
file.close()
print('updated!')
