from bs4 import BeautifulSoup
import requests

url = requests.get("")
soup = BeautifulSoup(url.content,"lxml")

print(soup)
