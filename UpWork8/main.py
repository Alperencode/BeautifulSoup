import requests
from bs4 import BeautifulSoup
import pandas as pd

# Didn't complete this job but I learned to use proxies even though I didn't use them in this job. 

masterlist = []

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
}

proxies = { 'http': "http://206.81.0.107:80"}

url = "https://www.yad2.co.il/realestate/forsale"
url = requests.get(url,headers=headers, proxies=proxies,timeout=10)
soup = BeautifulSoup(url.content,"lxml")

print(soup.prettify())

# df = pd.DataFrame(masterlist)
# datatoexcel = pd.ExcelWriter(f"bloomingdales.xlsx",engine='xlsxwriter')
# df.to_excel(datatoexcel,index=False)
# datatoexcel.save()