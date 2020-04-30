import socket
import re

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('iedcr.gov.bd', 80))
cmd = 'GET http://iedcr.gov.bd HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(10000)
    if len(data) < 1:
        break
    try:
        str = data.decode()
    except:
        continue
data = open('data.txt')
#print(len(str))
num = re.findall('<td>([0-9]+)</td>',str)
print('Test conducted in last 24 hours:',num[2],'\nTotal test conducted:',num[5])
print('COVID-19 positive in last 24 hours:',num[8],'\nTotal COVID-19 Positive:',num[11])
mysock.close()
