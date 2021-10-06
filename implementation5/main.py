from bs4 import BeautifulSoup
import requests

# gather the tables to excel

url = requests.get("https://www.nfl.com/stats/team-stats/offense/passing/2021/reg/all")
soup = BeautifulSoup(url.content,"lxml")

names = soup.find_all("div",class_="d3-o-club-fullname")

# for name in names:
#     print(name.text.strip())

table = soup.find("table").tbody
teams = table.tr.next_siblings

for i in teams:
    try:
        print(i.td)
    except:
        pass

