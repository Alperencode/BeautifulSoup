import requests, csv
from bs4 import BeautifulSoup

# Variables
requestCounter, errorCounter, sessionCounter, parseCounter = 0, 0, 0, 0
imageURLS = []
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
    
def SafeFind(soup, tag, class_=None, id=None):
    """Helper function to safely find element in soup"""
    if id:
        result = soup.find(tag, id=id)
    else:
        result = soup.find(tag, class_=class_)
    return result.text.strip() if result else ""

def ParseProductPage(url):
    """ Parses the product page and writes to CSV """
    global imageURLS, parseCounter
    dataDict = {}
    parseCounter += 1
    soup = SendRequest(url)

    # Product Info
    dataDict['Product URL'] = url
    dataDict['Product Title'] = SafeFind(soup, tag="h1", class_="product_title entry-title")
    dataDict['Product Description Short'] = SafeFind(soup, tag="div", class_="woocommerce-product-details__short-description")
    dataDict['Product Description Long'] = SafeFind(soup, tag="div", id="cgkit-tab-description")
    dataDict['SKU'] = SafeFind(soup, tag="span", class_="sku")

    # Product Price
    productPrices = SafeFind(soup, tag="p", selector="price")
    if productPrices:
        dataDict['Product Price'] = productPrices.findAll("del")[2].text.strip()
        dataDict['Product Sale Price'] = productPrices.find("ins").text.strip()

    # Category & Brand
    postedIn = SafeFind(soup, tag="span", class_="posted_in")
    if postedIn:
        dataDict['Category'] = postedIn[0].text.strip()
        dataDict['Brand'] = postedIn[1].text.strip()

    # Image URL
    imageUrl = soup.find("figure",class_="woocommerce-product-gallery__wrapper").img.get('src')
    imageURLS.append(imageUrl)
    dataDict['Image URL'] = imageUrl

    # Write to CSV
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


# Loops
for pageNumber in range(1, GetMaxPage()+1):
    url = f"https://service-workshopmanual.com/product-category/machine-vehicle-manuals/page/{pageNumber}"
    for url in ScrapeURL(url):
        try:
            ParseProductPage(url)
        except:
            errorCounter += 1
            print(f"Error: {url}")

for image in imageURLS:
    SaveImage(image, name=imageURLS.index(image)+1)

print(f"Total Sessions: {sessionCounter}")
print(f"Total Errors: {errorCounter}")
print(f"Total Parsed: {parseCounter}")