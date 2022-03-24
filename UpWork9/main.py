from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
import pandas as pd
import time

# -- Setting up the Selenium -- #
driver = Chrome(executable_path='chromedriver.exe')
driver.get('https://www.faire.com/category/Women/subcategory/Apparel/Printed%20Tees?filters=sorting%3Afeatured')

# -- Getting the source code -- #
time.sleep(10)
print("opened the url - Sleeping 10 secs")
print("Next - clicking the blank area")

# Need to click someting to trigger the javascript for login section because its blocking the source code that I need
# but it's a bit complicated. 

time.sleep(10)
print("clicked the blank area - Sleeping 10 secs")
print("Next - clicking close button")

button = driver.find_element_by_class_name('ModalNavigationAbsolute__CloseButton-sc-1xdujn8-0 kKGeKD closeButton')
button.click()

print("clicked the close button")
print("Next - scraping page with BeautifulSoup")


# -- Scraping  -- #
soup = BeautifulSoup(driver.page_source,"lxml")
names = soup.findAll("span",class_="DetailSection__Underline-sc-1h3ipst-0 OjYcm")

if names:
    for name in names:
        print(name.text.strip())
else:
    print("No names found")

driver.quit()

# Details for job:
# https://www.faire.com/category/Apparel/subcategory/Women/Printed%20Tees?filters=sorting%3Afeatured
# need the Companies name and location.