import requests
from bs4 import BeautifulSoup

def main():
    # Taking the input    
    search = str(input("Search: "))
    
    # Replacing spaces with +
    search = search.replace(" ","+") 
    
    # Creating the url
    url = f"https://www.google.com/search?q={search}"
    
    # Getting the source code
    url = requests.get(url)
    soup = BeautifulSoup(url.content, "lxml")

    # Scraping the data
    try:
        info = soup.find("div",class_="BNeawe s3v9rd AP7Wnd").text
        print("\n",info)
    except:
        print("\nNo results found")

if __name__ == "__main__":
    main()