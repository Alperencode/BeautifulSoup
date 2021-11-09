import requests
from bs4 import BeautifulSoup

session = requests.Session()
payload = {
        "keyword":"bilisim",
        "yil1":0,
        "yil2":0,
        "nevi":1,
        "tip":1,
        "Tur":0,
        "Dil":0,
        "ops_field":"and",
        "nevi2":1,
        "tip2":1,
        "izin":0,
        "Durum":3,
        "ops_field1":"and",
        "nevi3":1,
        "tip3":1,
        "Universite":0,
        "Enstitu":0,
        "islem":4,
        }

url = session.post('https://tez.yok.gov.tr/UlusalTezMerkezi/SearchTez',data=payload)
print(url.cookies)
soup = BeautifulSoup(url.content,"lxml")
print(soup)
