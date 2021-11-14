from bs4.dammit import xml_encoding
import requests
from bs4 import BeautifulSoup

url = requests.get("https://isthereanydeal.com")

soup = BeautifulSoup(url.content, "lxml")

GameNamesList = soup.find_all("a",class_='noticeable')
GamesStr = []
for GameNames in GameNamesList:
    GamesStr.append(GameNames.text.strip().lower().replace(" ", ""))

# ---- PUNCTATION REMOVE SECTION ----
GameNamesWithoutPunctuation = []
punctuation = ["'","!",",",":","®","™","-","+"]

# Road map to what i need to do?
# 1- a loop that inside game names
# 2- inside that loop another loop that inside names so we can check every chart that name has
# 3- if that loop detects any punctation remove the counter using index numbers  
# 4- go for another check if its still has punctation 
# 5- if it is remove it too if its not then add to the GameNamesWithoutPunctuation list

# to delete by using index --- strObj = strObj[0 : index : ] + strObj[index + 1 : :] 

for name in GamesStr:      # i inside the Game names 
    # Check 1
    for z in range(0,(len(name)-2)):    # z is starting from zero to lenght of name (I did -2 because otherwise its giving 'out of index' error )
        if name[z] in punctuation:  # if name has a punctation on its any index
            # Control Section 1
            if name in GameNamesWithoutPunctuation: # then check for if its in the list cause we need to remove it  
                GameNamesWithoutPunctuation.remove(name)    # if it is remove it
                name2 = name[0 : z : ] + name[z + 1 : :]    # delete the punctation

                # We going for another check if it still has punctation
                for q in range(0,(len(name2)-2)):
                    if name2[q] in punctuation:     # if name has a punctation on its any index
                        if name2 in GameNamesList:  # check again if its in the list 
                            GameNamesList.remove(name2)     # if it is then remove it
                            name3 = name2[0 : q : ] + name2[q + 1 : :]  # delete the punctation

                    else:  # if it has no punctation then check for if its already on list
                        if name2 in GameNamesWithoutPunctuation:    # if it is
                            pass                                    # just pass 
                        else:                                       # if its not
                            GameNamesWithoutPunctuation.append(name2)   # then add it
                        
            else:   # Its doing the exactly same thing that we did in Control Section 1
                # it just dont have a list.remove() line here
                name2 = name[0 : z : ] + name[z + 1 : :]
                for q in range(0,(len(name2)-2)):
                    if name2[q] in punctuation:     
                        if name2 in GameNamesList:
                            GameNamesList.remove(name2)
                            name3 = name2[0 : q : ] + name2[q + 1 : :]
                    else:
                        if name2 in GameNamesWithoutPunctuation:
                            pass
                        else:
                            GameNamesWithoutPunctuation.append(name2)

        else:
            if name in GameNamesWithoutPunctuation:
                pass
            else:
                GameNamesWithoutPunctuation.append(name)


print(GameNamesWithoutPunctuation)
for t in GameNamesWithoutPunctuation:
    print(t)

# ---- Getting div tags for prices ----
DivTagsList = []
PriceDivTags = soup.find_all("div",class_="deals dyn-semi")
for i in PriceDivTags:
    DivTagsList.append(i)

# ---- Div prettify() to look inside ----
for z in DivTagsList:
    print(z.prettify())

# ---- Game prices ----
aTags = soup.select('a[class^="shop"]')
for k in aTags:
    print(k)

