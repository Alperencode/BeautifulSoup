import requests     
from bs4 import BeautifulSoup
import time

r = requests.get('https://isthereanydeal.com')      # Send get request to my linkedin profile and store it in 'r' variable
soup = BeautifulSoup(r.content, "lxml")         # created a new variable and store the source code of 'r'


# --- Using Find method
#print(soup.find("span").text.strip())       # find is gonna return first and 'one' variable that we give to it

#for x in soup.find_all("span"):     # to pull all the tags that we trying to find we'll use find_all()
#    print(x)

print("")
# --- Customizing the search
games = soup.find("div",attrs={"class":"title"}) # to customize our search we give attrs={} variable to find
print(games)
      

# ----------------------------------------------------------------------------------------------------
# Its just a mistake that i made because i did not understand how find works at the begining
# !!! Find is not working like: Yeah i found this div now im inside in it so you have to make another for loop to find the other class 

#games = soup.find_all("div",attrs={"class":"game"}) 
#for game in games:
#    gametitles = game.find_all("div",attrs={"class":"title"}) 
#    for x in gametitles:
#        print(x.find("a",attrs={"class":"noticeable"}).text)

# ----------------------------------------------------------------------------------------------------

# Finds works like: you just need to name the tag and class
# Find is already searching the whole source code either you specify all divs or not 
gamenames = soup.find_all("a",attrs={"class":"noticeable"}, limit=10)
for game in gamenames:
    print("Game name: {}".format(game.text))
    print("Redirecting to {}\n".format(game.get("href")))
