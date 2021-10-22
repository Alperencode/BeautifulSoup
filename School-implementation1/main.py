from bs4 import BeautifulSoup
import time
import requests
import pandas as pd
data_list = []


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

for pageNumber in range(1,last_page+1):
    get_pages(pageNumber)

for url in linkList:
    get_magazine_links(url)

# --------- Gathering Links End ---------

# --------- Check "roman" and "yayın" ---------

# articles links which includes "roman"
checked_links = []

def createDataDict(checkledLink):
    url = requests.get(checkledLink)
    soup = BeautifulSoup(url.content,"lxml")
    dataDict = {}
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
    # if dataDict not in data_list:
    #     data_list.append(dataDict)

def get_roman_articles(magazineLink):
    url = requests.get(magazineLink)
    soup = BeautifulSoup(url.content,"lxml")

    labels = soup.find_all("a",class_="card-title article-title")
    for label in labels:
        # removing row number and creating string var for labels to check "roman"
        labelText = label.text.split(".")
        labelText.pop(0)
        labelText = ' '.join(labelText)
        labelText = labelText.replace("\n","").lower()
        if "roman" in labelText:
            url = f"https:{label.get('href')}"
            url = requests.get(url)
            soup = BeautifulSoup(url.content,"lxml")
            ozet_section = soup.find("div",class_="article-abstract data-section")
            print(url)
            ozet_pTags = ozet_section.find_all("p")
            for ozet in ozet_pTags:
                if "yayın" not in ozet.text.lower():
                    createDataDict(f"https:{label.get('href')}")

for magazinLink in magazine_links:
    get_roman_articles(magazinLink)

# --------- Check "roman" and "yayın" End ---------

# --------- Output to Excel ---------

df = pd.DataFrame(data_list)
File_Name = "Article_Data"
datatoexcel = pd.ExcelWriter(f"{File_Name}.xlsx",engine='xlsxwriter')
df.to_excel(datatoexcel,index=False)
datatoexcel.save()

# --------- Output to Excel End ---------

# romanLinkleri = ["https://dergipark.org.tr/tr/pub/19maysbd/issue/65148/960736","https://dergipark.org.tr/tr/pub/ak/issue/63406/941413","https://dergipark.org.tr/tr/pub/medalanya/issue/64601/895129","https://dergipark.org.tr/tr/pub/gaziaot/issue/64759/815831","https://dergipark.org.tr/tr/pub/adalya/issue/61897/837795",
# "https://dergipark.org.tr/tr/pub/aduefebder/issue/63241/877766","https://dergipark.org.tr/tr/pub/akusosbil/issue/64981/873870","https://dergipark.org.tr/tr/pub/aicusbed/issue/61279/910019","https://dergipark.org.tr/tr/pub/apdad/issue/63126/824066","https://dergipark.org.tr/tr/pub/asbider/issue/65093/1000775",
# "https://dergipark.org.tr/tr/pub/akaded/issue/62203/937493","https://dergipark.org.tr/tr/pub/akademik-hassasiyetler/issue/64679/922714","https://dergipark.org.tr/tr/pub/akademiksanat/issue/64719/898278","https://dergipark.org.tr/tr/pub/akademiksanat/issue/64719/898278",
# "https://dergipark.org.tr/tr/pub/ktc/issue/62579/926317","https://dergipark.org.tr/tr/pub/akrajournal/issue/64897/881924","https://dergipark.org.tr/tr/pub/akrajournal/issue/64897/904068"]
