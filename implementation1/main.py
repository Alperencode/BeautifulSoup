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

ctg = soup.find_all("a",class_="dropdown-item")
ctglist = []

for i in ctg:
    print(i.text)
    if(i.get('href') == "/Register" or i.text == "Forgot password?"):
        pass
    else:
        ctglist.append(i.text)

    # data_dict['category'] = i.text
    # masterlist.append(data_dict)

print(ctglist)

# print(data_dict)
    


# Will add: i need to create a column named Category and add the ctglist values as a line
# For now if i try to add them as a line its only adding the last value for all lines
# for example:

for z in ctglist:
    data_dict['category'] = z
    masterlist.append(data_dict)

# print(masterlist)
df = pd.DataFrame(masterlist)
print(df)

# so for now i can gather the data but cant list for pandas table
# and to output as excel file i need to use pandas
