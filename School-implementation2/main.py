import requests
from bs4 import BeautifulSoup

session = requests.Session()
payload = {
        "keyword":"bilisim",
        }
url = session.post('https://tez.yok.gov.tr/UlusalTezMerkezi/SearchTez',data=payload)

print(url)
print(url.cookies)
soup = BeautifulSoup(url.content,"lxml")
print(soup)
