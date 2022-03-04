import requests
from bs4 import BeautifulSoup

masterlist = []

url = "https://all.accor.com/de/country/hotels-deutschland-pde.shtml"
url = requests.get(url)
soup = BeautifulSoup(url.content,"lxml")

aTags = soup.findAll("a",class_="Teaser-link")

for i in aTags:
    dataDict = {}
    print(i.get('href'))
    dataDict['name'] = i.text.strip()
    masterlist.append(dataDict)

print(masterlist)