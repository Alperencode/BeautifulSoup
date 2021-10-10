from bs4 import BeautifulSoup
from numpy import False_
import pandas as pd
import requests

# gather the tables to excel

url = requests.get("https://www.nfl.com/stats/team-stats/offense/passing/2021/reg/all")
soup = BeautifulSoup(url.content,"lxml")

masterList = []
nameList = []

names = soup.find_all("div",class_="d3-o-club-fullname")

for name in names:
    nameList.append(name.text.strip())

table = soup.find("table").tbody
teams = table.tr.next_siblings

for team in teams:
    try:
        skill_Dict = {}
        name = team.find("div",class_="d3-o-club-fullname").text.strip()
        skills = team.find_all("td")
        skill_Dict['Full Name'] = name
        skill_Dict['Att'] = skills[1].text.strip()
        skill_Dict['Cmp'] = skills[2].text.strip()
        skill_Dict['Cmp%'] = skills[3].text.strip()
        skill_Dict['Yds/Att'] = skills[4].text.strip()
        skill_Dict['Pass Yds'] = skills[5].text.strip()
        skill_Dict['TD'] = skills[6].text.strip()
        skill_Dict['INT'] = skills[7].text.strip()
        skill_Dict['Rate'] = skills[8].text.strip()
        skill_Dict['1st'] = skills[9].text.strip()
        skill_Dict['1st%'] = skills[10].text.strip()
        skill_Dict['20+'] = skills[11].text.strip()
        skill_Dict['40+'] = skills[12].text.strip()
        skill_Dict['Lng'] = skills[13].text.strip()
        skill_Dict['Sck'] = skills[14].text.strip()
        skill_Dict['SckY'] = skills[15].text.strip()
        masterList.append(skill_Dict)
    except:
        pass
for name in nameList:
    print(f"Team {name} added...")

df = pd.DataFrame(masterList)
File_Name = "Team_Statistics"
datatoexcel = pd.ExcelWriter(f"{File_Name}.xlsx",engine='xlsxwriter')
df.to_excel(datatoexcel,index=False)
datatoexcel.save()
