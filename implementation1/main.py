import pandas as pd
import requests
from bs4 import BeautifulSoup
# ----- How to make excel
masterlist = []
data_dict = {"Category":[], "Sub Category":[]}
# data_dict['category1'] = value1
# # data_dict['category2'] = value2 
# # masterlist.append(data_dict)
# df = pd.DataFrame(masterlist) # to see datas
# df.to_csv('Name') # to excel

# Gathering Server Data
url = requests.get("https://www.serversupply.com")
soup = BeautifulSoup(url.content, "lxml")
# ------------------------------------


ctg = soup.find_all("li")

for i in ctg[6].next_siblings:
    data_dict["Category"] = i.text.strip()
  
print(data_dict)

# print(masterlist)
df = pd.DataFrame(masterlist)
#print(df)

# so for now i can gather the data but cant list for pandas table
# and to output as excel file i need to use pandas
