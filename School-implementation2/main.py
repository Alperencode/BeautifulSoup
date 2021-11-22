import requests
from bs4 import BeautifulSoup
s = requests.Session()
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
    'name':f'{str(session_cookie[0])}',
    'value':f'{str(session_cookie[1])}'
    #'name':'JSESSIONID',
    #'value': '"bPuY8quhUIhyL3lC19WdK_mbXczlSz8bsEETq2Wt.jbossn182:TEZ_8150"'
}
print(req_args)
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
JSESSIONID="bPuY8quhUIhyL3lC19WdK_mbXczlSz8bsEETq2Wt.jbossn182:TEZ_8150"