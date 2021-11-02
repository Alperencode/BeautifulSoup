import requests
from bs4 import BeautifulSoup

session = requests.Session()

jar = requests.cookies.RequestsCookieJar()
jar.set('JSESSIONID','"R6BD0hbICZ2gGiLeqvjhlO-kFP2Ko3y4i3Rxk2jX.jbossn183:TEZ_8150"; TS01e18b4b=01026844b842721713e4bf5b2fff46eb8572168e0ddb424608cfaaa87a20f40c847056a6f101079411d0457c55b06c0f463672ee6116b3f36b3cfc24ed565c005fb42d5040; _ga=GA1.3.1694449284.1635759066; _gid=GA1.3.1885659291.1635759066; _gat=1; TS014c3a3f=01026844b87977383618aa452990ea860125b94583bb4f2532334fc5ff218cd61bf1cfee0705eca67d30d3b01931628ed04ebab2fe; TScee0d053027=0868d5a3ffab20009499254fe5bfc63e0f684b690cc763aafa9fbc0373d8bef64791b04ae8d599d208efbfff00113000c7aac62fd4c1f39e15169939df45fed3987ec7ebaab22dd5ecc127b2345044f7978760407b786dc912a0fbcbeeab0d33')

session.cookies = jar

url = session.get('https://tez.yok.gov.tr/UlusalTezMerkezi/tezSorguSonucYeni.jsp')
soup = BeautifulSoup(url.content, "lxml")

print(soup)
