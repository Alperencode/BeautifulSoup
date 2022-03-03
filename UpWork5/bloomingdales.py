import requests
from bs4 import BeautifulSoup
import pandas as pd

masterlist = []

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
}
url = "https://www.bloomingdales.com/shop/all-designers?id=1001351&cm_sp=NAVIGATION-"
url = requests.get(url,headers=headers)
soup = BeautifulSoup(url.content,"lxml")

aTags = soup.findAll("a",class_="brand_link")

for i in aTags:
    dataDict = {}
    print(i.text.strip())
    dataDict['Company Name'] = i.text.strip()
    masterlist.append(dataDict)


df = pd.DataFrame(masterlist)
datatoexcel = pd.ExcelWriter(f"bloomingdales.xlsx",engine='xlsxwriter')
df.to_excel(datatoexcel,index=False)
datatoexcel.save()