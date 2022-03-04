import requests
from bs4 import BeautifulSoup
s = requests.Session()

my_cookie = requests.cookies.create_cookie(**req_args)
s.cookies.set_cookie(my_cookie)
print(s.cookies)

url = s.get('https://pubs.acs.org/doi/full/10.1021/acschembio.1c00993',cookies=s.cookies)
soup = BeautifulSoup(url.content,"lxml")

spans = soup.find_all('span',attrs={'class':'hlFld-ContribAuthor'})
for i in spans:
    print(i.text)