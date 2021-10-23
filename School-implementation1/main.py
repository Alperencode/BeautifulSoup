from bs4 import BeautifulSoup
import requests
import pandas as pd
data_list = []
counter = 0

# --------- Gathering Links ---------
linkList = []
magazine_links = []

# Parsing first page to get last page number
url = "https://dergipark.org.tr/tr/search?q=&section=journal"
url = requests.get(url)
soup = BeautifulSoup(url.content,"lxml")

# Gathering last page number 
page_slider = soup.find("ul",class_="kt-pagination__links mx-auto")
last_page = int(page_slider.find_all("li")[-2].text)
del url

# Generating links for all pages
def get_pages(pageNumber):
    url = f"https://dergipark.org.tr/tr/search/{pageNumber}?q=&section=journal"
    linkList.append(url)

# Gathering each magazine link
def get_magazine_links(url):
    url = requests.get(url)
    soup = BeautifulSoup(url.content,"lxml")
    # finding all magazines
    magazines = soup.find_all("h5",class_="card-title")
    for link in magazines:
        magazine_links.append(link.a.get('href'))

# range loop for use get_pages function
for pageNumber in range(1,last_page+1):
    get_pages(pageNumber)

# using get_magazine_links function
for url in linkList:
    get_magazine_links(url)
# --------- Gathering Links End ---------

# --------- Check "roman" and "yayın" ---------
# gathering infos if the article passes the check 
def createDataDict(checkledLink):
    url = requests.get(checkledLink)
    soup = BeautifulSoup(url.content,"lxml")
    dataDict = {}
    global counter
    counter += 1

    # Makale Başlığı
    article_title = soup.find("h3",class_="article-title").text.strip()
    dataDict['Makale Başlığı'] = article_title

    # Yazar İsimleri
    article_authors = soup.find("p",class_="article-authors")
    try:
        names = []
        author_names = article_authors.find_all("a",class_="is-user")
        for name in author_names:
            names.append(name.text.strip())
        dataDict['Yazar İsimleri'] = names
    except: 
        author_name = article_authors.find("a").text.strip()
        dataDict['Yazar İsimleri'] = author_name


    # Yayın Yılı
    # Not: Yayın yılının değeri için class belirtilmediği için bulunduğu tabloyu çektim, <tr> taglarını aldım, <tr> taglarının içindeki değerlerden kontrol yaptım
    info_table = soup.find("table",class_="record_properties table")
    tr_tags = info_table.find_all("tr")
    for tr_tag in tr_tags:
        if tr_tag.th.text.strip() == "Yayımlanma Tarihi":
            dataDict['Yayın Yılı'] = tr_tag.td.text.strip()

    # Dergi İsmi
    magazine_name = soup.find("h1",attrs={"id":"journal-title"}).text.strip()
    dataDict['Dergi İsmi'] = magazine_name

    # Yayın Sayfa URL
    page_url = checkledLink
    dataDict['Yayın Sayfa URL'] = page_url

    # Yayın PDF'i
    tool_bar = soup.find("div", attrs={"id":"article-toolbar"})
    a_tags = tool_bar.find_all("a")
    shortLink = a_tags[0].get("href")
    pdf_link = f"https://dergipark.org.tr{shortLink}"
    dataDict['Yayın PDF'] = pdf_link
    
    data_list.append(dataDict)
    print(f"{counter}. Article created")

# Checking articles
def checkFunc(magazineLink):
    url = requests.get(magazineLink)
    soup = BeautifulSoup(url.content,"lxml")

    labels = soup.find_all("a",class_="card-title article-title")
    for label in labels:
        # removing row number and creating string variable for labels to check "roman"
        labelText = label.text.split(".")
        labelText.pop(0)
        labelText = ' '.join(labelText)
        labelText = labelText.replace("\n","").lower()
        if "roman" in labelText:
            url = f"https:{label.get('href')}"
            url = requests.get(url)
            soup = BeautifulSoup(url.content,"lxml")
            ozet_section = soup.find("div",class_="article-abstract data-section")
            ozet_pTags = ozet_section.find_all("p")
            # Created check bool to avoid making dict of same article
            check = True
            for ozet in ozet_pTags:
                if "yayın" not in ozet.text.lower():
                    check = True
                else:
                    check = False
            # if check true -> create dict
            if check:
                createDataDict(f"https:{label.get('href')}")

for magazinLink in magazine_links:
    checkFunc(magazinLink)
# --------- Check "roman" and "yayın" End ---------

# --------- Output to Excel ---------
dataFrame = pd.DataFrame(data_list)
File_Name = "Article_Data"
datatoexcel = pd.ExcelWriter(f"{File_Name}.xlsx",engine='xlsxwriter')
dataFrame.to_excel(datatoexcel,index=False)
datatoexcel.save()
# --------- Output to Excel End ---------