# Just started, didn't finished yet.
import requests
from bs4 import BeautifulSoup

def main():
    
    # need to get this id automatically
    # making it constant for now
    id = 9206

    # Creating the url
    url = f"https://namazvakitleri.diyanet.gov.tr/tr-TR/{id}"

    # Getting the source code
    url = requests.get(url)
    soup = BeautifulSoup(url.content, "lxml")

    table = soup.find("table", class_="table vakit-table")

    tdTags = table.findAll("td")
    masterlist = []
    dataDict = {}

    # main objective is here is making dict with 2 keys
    # date: date-value
    # time: all times for that date 
    for i in tdTags:
        if len(i.text.strip()) > 5:
            if dataDict:
                masterlist.append(dataDict)
            dataDict['date'] = i.text.strip()
        else:
            dataDict['time'] = i.text.strip()
    print(masterlist)

if __name__ == "__main__":
    main()