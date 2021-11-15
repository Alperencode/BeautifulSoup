import requests
from bs4 import BeautifulSoup
s = requests.Session()
print(s.cookies)
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

url = s.post('https://tez.yok.gov.tr/UlusalTezMerkezi/SearchTez',data=payload)
session_cookie = url.cookies.items()[1]
print(session_cookie[0])
print(session_cookie[1])
req_args = {
    'name':f'{session_cookie[0]}',
    'value':f'{session_cookie[1]}'
}

optional_args = {
    'domain':'tez.yok.gov.tr',
    'path':'/UlusalTezMerkezi',
}

my_cookie = requests.cookies.create_cookie(**req_args,**optional_args)
s.cookies.set_cookie(my_cookie)
print(s.cookies)

url = s.get('https://tez.yok.gov.tr/UlusalTezMerkezi/tezSorguSonucYeni.jsp',cookies=s.cookies)

soup = BeautifulSoup(url.content,"lxml")
print(soup.prettify()) 