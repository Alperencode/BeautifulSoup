import requests, csv
from bs4 import BeautifulSoup

requestCounter, errorCounter, sessionCounter, parseCounter = 0, 0, 0, 0
imageURLS, masterList = [], []
MAX_REQUEST = 100
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

# Initials
session = requests.Session()
with open("output.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["URL", "Title", "Sale Price", "Price", "SKU", "Category", "Brand", "Image URL", "Description Short", "Description Long"])

# Functions
def ChangeSession():
    global session, sessionCounter
    """
    Changes the session to avoid connection errors
    [Eg: 429 - Too Many Requests]
    """
    sessionCounter += 1
    session = requests.Session()

def SendRequest(url):
    """
    Sends a request to the given url
    """
    global requestCounter, errorCounter
    if requestCounter > MAX_REQUEST:
        ChangeSession()
        requestCounter = 0
    try:
        url = session.get(url, headers=headers)
        requestCounter += 1
    except Exception as e:
        errorCounter += 1
        print(f"Error: {e}")
        return
    return BeautifulSoup(url.content,"lxml")

def ScrapeURL(url):
    productLinks = []
    soup = SendRequest(url)
    products = soup.findAll("a", class_="woocommerce-LoopProduct-link woocommerce-loop-product__link")
    for i in set(products):
        productLinks.append(i.get('href'))
    return set(productLinks)

def GetMaxPage():
    url = "https://service-workshopmanual.com/product-category/machine-vehicle-manuals/"
    soup = SendRequest(url)
    PageNumbers = soup.findAll("a",class_="page-numbers")
    maxPage = PageNumbers[-2].text.strip()
    return int(maxPage.replace(",",""))

def SaveImage(url, name):
    img = session.get(url, headers=headers)
    with open(f"images/{name}.jpg", "wb") as f:
        f.write(img.content)
    
def ParseProductPage(url):
    global imageURLS
    dataDict = {}
    global parseCounter
    parseCounter += 1
    soup = SendRequest(url)

    dataDict['Product URL'] = url

    try:
        productTitle = soup.find("h1",class_="product_title entry-title").text.strip()
    except:
        productTitle = ""
    dataDict['Product Title'] = productTitle

    try:
        productDescriptionShort = soup.find("div",class_="woocommerce-product-details__short-description").text.strip()
    except:
        productDescriptionShort = ""
    dataDict['Product Description Short'] = productDescriptionShort

    try:
        productDescriptionLong = soup.find("div", id="cgkit-tab-description").text.strip()
    except:
        productDescriptionLong = ""
    dataDict['Product Description Long'] = productDescriptionLong

    try:
        productPrices = soup.find("p",class_="price")
    except:
        productPrices = ""

    try:
        productPrice = soup.findAll("del")[2].text.strip()
    except:
        productPrice = ""
    dataDict['Product Price'] = productPrice

    try:
        productSalePrice = productPrices.ins.text.strip()
    except:
        productSalePrice = ""
    dataDict['Product Sale Price'] = productSalePrice

    try:
        sku = soup.find("span",class_="sku").text.strip()
    except:
        sku = ""
    dataDict['SKU'] = sku

    try:
        postedIn = soup.findAll("span",class_="posted_in")
    except:
        postedIn = ""

    try:
        category = postedIn[0].text.strip()
    except:
        category = ""
    dataDict['Category'] = category

    try:
        brand = postedIn[1].text.strip()
    except:
        brand = ""
    dataDict['Brand'] = brand

    try:
        imageUrl = soup.find("figure",class_="woocommerce-product-gallery__wrapper").img.get('src')
        imageURLS.append(imageUrl)
    except:
        imageUrl = ""
    dataDict['Image URL'] = imageUrl

    with open("output.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            dataDict['Product URL'],
            dataDict['Product Title'],
            dataDict['Product Sale Price'],
            dataDict['Product Price'],
            dataDict['SKU'],
            dataDict['Category'],
            dataDict['Brand'],
            dataDict['Image URL'],
            dataDict['Product Description Short'],
            dataDict['Product Description Long']
        ])

    return dataDict

# Loops
for pageNumber in range(1, GetMaxPage()+1):
    url = f"https://service-workshopmanual.com/product-category/machine-vehicle-manuals/page/{pageNumber}"
    for url in ScrapeURL(url):
        masterList.append(ParseProductPage(url))

for image in imageURLS:
    SaveImage(image, name=imageURLS.index(image)+1)

print(f"Total Sessions: {sessionCounter}")
print(f"Total Errors: {errorCounter}")
print(f"Total Parsed: {parseCounter}")