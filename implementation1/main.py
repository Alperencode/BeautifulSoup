import pandas as pd
import requests
from bs4 import BeautifulSoup
# ----- How to make excel
masterlist = []
data_dict = {}
# data_dict['category1'] = value1
# # data_dict['category2'] = value2 
# # masterlist.append(data_dict)
# df = pd.DataFrame(masterlist) # to see datas
# df.to_csv('Name') # to excel

url = requests.get("https://www.serversupply.com/HARD%20DRIVES")

soup = BeautifulSoup(url.content, "lxml")

Categories = soup.find_all("a",class_="dropdown-item")

for i in Categories:
    print(i.text)
    data_dict['category'] = i.text
    masterlist.append(data_dict)

# print(masterlist)
df = pd.DataFrame(masterlist)
print(df)

# Here is the bug === its adding only last category to master list
# And its gathering first two menu which is not category