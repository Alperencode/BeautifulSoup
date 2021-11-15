from requests.structures import CaseInsensitiveDict
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
# headers = CaseInsensitiveDict()
# headers["Cookie"] =  'JSESSIONID="Cy0gHV4QN6DjdtbMEhPA5LlR4nIVwSo8z08H8RoV.jbossn183:TEZ_8150"';"TS01e18b4b=01026844b8c67d161539dfd8f5dd42d826cefa534f246868374012faf21e9e808d265c9a84f883a0f5fd8c3c097c6980d447638982213fdf0889e4bcc245ff69a7b98cb035";"TS014c3a3f=01026844b832c2fe02e63442694aa776005d952617246868374012faf21e9e808d265c9a848b2fd624a0bf5034cf8eb36ee901369a"


cookieValue = url.cookies.items()[1][1].replace('"',"")
# print(url.cookies.items())
print(url.cookies.items()[1])
url.cookies.set("JSESSIONID", '"7FztOsTP9iPAiSFPFSTzw5FQnjlF7IZwdkGa7Zzo.jbossn183:TEZ_8150"', domain="tez.yok.gov.tr")
url2 = session.get("https://tez.yok.gov.tr/UlusalTezMerkezi/tezSorguSonucYeni.jsp",cookies = url.cookies)
soup = BeautifulSoup(url2.content,"lxml")
# print(url2.cookies)
# print(soup.prettify())
# print(url.cookies)
# print(url.cookies.items()[1][1])
# url2 = requests.get("https://tez.yok.gov.tr/UlusalTezMerkezi/tezSorguSonucYeni.jsp",)