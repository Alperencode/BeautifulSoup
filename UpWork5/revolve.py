import requests
from bs4 import BeautifulSoup
import pandas as pd

masterlist = []

url = "https://www.revolve.com/designers/?orderBy=A-Z&navsrc=main&d=Womens#123"
url = requests.get(url)
soup = BeautifulSoup(url.content,"lxml")

aTags = soup.findAll("a",class_="u-margin-l--lg")

for i in aTags:
    dataDict = {}
    print(i.text.strip())
    dataDict['Company Name'] = i.text.strip()
    masterlist.append(dataDict)


df = pd.DataFrame(masterlist)
datatoexcel = pd.ExcelWriter(f"revolve.xlsx",engine='xlsxwriter')
df.to_excel(datatoexcel,index=False)
datatoexcel.save()