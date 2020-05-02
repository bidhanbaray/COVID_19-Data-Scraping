from geojson import Point, Feature, FeatureCollection, dump
import urllib.request, urllib.parse, urllib.error
import json
import ssl
import PyPDF2
import re

pdfFileObj = open('data_update.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#print(pdfReader.numPages)
pageObj = pdfReader.getPage(1)
#print(pageObj.extractText())
content = pageObj.extractText()
contentList = content.split('\n \n')
pdfFileObj.close()
#print(contentList)
startindex = contentList.index('Total')
del contentList[0:startindex+1]

contentDict = dict()
i = 0;
while i<len(contentList)-1:
    contentDict[contentList[i].replace('\n','').lower()] = contentList[i+1]
    i+=2
#print(contentDict)
print ('reading done')
serviceurl = 'http://py4e-data.dr-chuck.net/json?'
api_key = 42
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

features = []
for location,affected in contentDict.items():
    parms = dict()
    parms['address'] = location+', Dhaka'
    parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    try:
        js = json.loads(data)
    except:
        js = None
    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    #print(lat,lng)
    point = Point((lng,lat))
    if (int(affected)<=5):
        size = "small"
        clr = "#ffe7e6"
    elif (int(affected)<=15):
        size = "small"
        clr = "#ffb0ab"
    elif int(affected)<=30:
        size = "small"
        clr = "#ff5349"
    elif (int(affected)<=50):
        size = "small"
        clr = "#ff1b0e"
    elif int(affected)<=75:
        size = "small"
        clr = "#d20c00"
    elif int(affected)<=100:
        size = "small"
        clr = "#840700"
    elif (int(affected)<=250):
        size = "small"
        clr = "#5d0500"
    elif int(affected)<=500:
        size = "small"
        clr = "#350300"
    else:
        size = "small"
        clr = "#0e0100"
    features.append(Feature(geometry=point, properties={"marker-color": clr,\
                            "marker-size": size,\
                            "marker-symbol": ""}))
feature_collection = FeatureCollection(features)
with open('coronaMap_Dhaka.geojson', 'w') as f:
   dump(feature_collection, f)
print('json file generated! Success!')
