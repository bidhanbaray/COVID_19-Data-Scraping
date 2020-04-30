#reading pdf from online
import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import PyPDF2
import re

website = "https://iedcr.gov.bd/"
print('Requesting Access to',website,'... ...')
webPage = urllib.request.urlopen(website).read()
soupObject = BeautifulSoup(webPage,'html.parser')
anchorTags = soupObject('a')
url = anchorTags[0].get('href',None)
link2 = website+url
print('Opening distribution pdf from '+link2)
print('Reading Data... ... Please Wait.')


#link2 = "https://iedcr.gov.bd/website/images/files/nCoV/Case_dist_30_april_update.pdf"
handle = urllib.request.urlopen(link2).read()

file = open('case_dist.pdf','wb')
file.write(handle)
file.close()
pdfFileObj = open('case_dist.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#print(pdfReader.numPages)
pageObj = pdfReader.getPage(1)
#print(pageObj.extractText())
content = pageObj.extractText()
contentList = content.split('\n \n')
pdfFileObj.close()
#contentList = re.findall('(?ms)/S.+[0-9]+',content[82:])
# print(content[82:])
#print(contentList)

contentDict = dict()
i = 5;
while i<len(contentList)-1:
    contentDict[contentList[i].replace('\n','').lower()] = contentList[i+1]
    i+=2
#print(contentDict)
# for location,affected in contentDict.items():
#     print(location,affected)
print('Information collecting: DONE')
while True:
    location = input("Enter Location: ")
    if (len(location)<1):
        break;
    try:
        print('COVID-19 Patients in',location+':',contentDict[location.lower()])
    except:
        print("Location not found in Dhaka. Check spelling")
