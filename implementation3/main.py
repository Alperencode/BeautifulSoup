import requests
from bs4 import BeautifulSoup

masterlist = []

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
}

url = "https://www.hepsiemlak.com/ankara"
url = requests.get(url,headers=headers)
soup = BeautifulSoup(url.content,"lxml")

cards = soup.findAll("a",class_="card-link")

linkList = []

for card in cards:
    linkList.append(f"https://www.hepsiemlak.com{card.get('href')}")

for link in linkList:
    url = requests.get(link,headers=headers)
    soup = BeautifulSoup(url.content,"lxml")
    print(link)
    p = soup.find("p",class_="fontRB fz24 price")
    print(p.text.strip())