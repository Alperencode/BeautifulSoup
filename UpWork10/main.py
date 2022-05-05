import requests
from bs4 import BeautifulSoup

session = requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
}

url = session.get("https://app.dealroom.co/companies?applyDefaultFilters=true",headers=headers)

req_args = {
    'name':'dealroom-cookies',
    'value': '{"necessary":true,"preferences":true,"statistics":true,"marketing":true,"timestamp":"Thu, 05 May 2022 18:48:34 GMT"}'
}
# print(req_args)

my_cookie = requests.cookies.create_cookie(**req_args)
session.cookies.set_cookie(my_cookie)
print(session.cookies)

soup = BeautifulSoup(url.content,"lxml")
div = soup.find('div', class_="user-info-name")

print(div.text)