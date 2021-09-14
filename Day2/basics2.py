from bs4.dammit import xml_encoding
import requests
from bs4 import BeautifulSoup

url = requests.get("https://isthereanydeal.com")

soup = BeautifulSoup(url.content, "lxml")

GameNamesList = soup.find_all("a",class_='noticeable')
GamesStr = []
for GameNames in GameNamesList:
    GamesStr.append(GameNames.text.strip().lower().replace(" ", ""))
GameNamesWithoutPunctuation = []
punctuation = ["'","!",",",":","®","™","-","+"]

# liste 3 değeri de alıyor bir check yap eğer içinde noktalama varsa eklemesin 
for i in GamesStr:      # i inside the Game names 
    for x in punctuation:       # x inside punctuations
        if x in i:      # if game name has punctuation
            replacedNames = i.replace("{}".format(x),"")
            for z in punctuation: 
                if z in replacedNames:
                    replacedNames2 = replacedNames.replace("{}".format(z),"")
                    if replacedNames2 in GameNamesWithoutPunctuation:
                        pass
                    else:
                        GameNamesWithoutPunctuation.append(replacedNames2)
                    # print(f"Game Name: {replacedNames2}\n")
                else:
                    if replacedNames in GameNamesWithoutPunctuation:
                        pass
                    else:
                        GameNamesWithoutPunctuation.append(replacedNames)
                    # print(f"Game Name: {replacedNames}\n")
        else:
            pass
for t in GameNamesWithoutPunctuation:
    print(t)

    


# ---- Getting div tags for prices 
# DivTagsList = []
# PriceDivTags = soup.find_all("div",class_="deals dyn-semi")
# for i in PriceDivTags:
#     DivTagsList.append(i)

# for z in DivTagsList:
#     print(z.prettify())

# ---- Game prices ----
# aTags = soup.select('a[class^="shop"]')
# for k in aTags:
#     print(k)

