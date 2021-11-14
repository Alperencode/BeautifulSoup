from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.smartrmail.com/blog/shopify-clothing-stores/"
url = requests.get(url)
soup = BeautifulSoup(url.content,"lxml")
h3Tags = soup.findAll("h3")
aTags = soup.findAll("a")
linkList = []
masterlist = []
counter = 0 
for aTag in aTags: 
    try:   
        if aTag.text[0] == "V":
            link = aTag.get("href")
            linkList.append(link)
    except:
        pass
for h3 in h3Tags:
    dataDict = {}
    dataDict['Index'] = counter+1
    dataDict['Name'] = h3.text
    dataDict['Url'] = linkList[counter] 
    print(f"{counter+1}. {h3.text}\nurl: {linkList[counter]}")
    counter += 1
    masterlist.append(dataDict)

df = pd.DataFrame(masterlist)
datatoexcel = pd.ExcelWriter(f"shopify.xlsx",engine='xlsxwriter')
df.to_excel(datatoexcel,index=False)
datatoexcel.save()