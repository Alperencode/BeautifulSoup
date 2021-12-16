from bs4 import BeautifulSoup
import requests

# This is project did not finished because of client unresponsiveness
# but gained control of the main site just didn't scrape the data we need

url = "https://www.entrepreneur.com/franchises/500/2021/1"
url = requests.get(url)
soup = BeautifulSoup(url.content, "lxml")
nameList = []
linkList = []

Blues = soup.find_all("li",class_="border-b border-grey-100 hover:bg-blue-50")
Greys = soup.find_all("li",class_="border-b border-grey-100 bg-gray-50 hover:bg-blue-50")

def RemovePuncture(string):
    punctures = ["!","'","^","+","%","/","-",",",".",":",";"]
    for puncture in punctures:
        if puncture in string:
            string = string.replace(puncture,"")
    return string

for grey in Greys:
    name = grey.find("p",class_="text-base font-medium text-gray-700 truncate w-1/2")
    link = grey.find("a",class_="block").get('href')
    name = name.text.strip()
    if "Request Info" in name:
        name = name.replace("Request Info","").strip()
    linkList.append(link)
    nameList.append(name)


for blue in Blues:
    name = blue.find("p",class_="text-base font-medium text-gray-700 truncate w-1/2")
    link = blue.find("a",class_="block").get('href')
    name = name.text.strip()
    if "Request Info" in name:
        name = name.replace("Request Info","").strip()
    linkList.append(link)
    nameList.append(name)

def ScrapePage(link):
    url = f"https://www.entrepreneur.com/{link}"
    
    # Datas that need to be scraped

    # ranking = 
    # name =
    # related_categories =
    # initial_investment =
    # industry = 
    # founded = 
    # parent_company = 
    # leadership = 
    # ticker_symbol = 
    # franchising_since = 
    # of_employees_at_HQ = 
    # of_units = 
    # growth_over_3years = 
    # corporate_address = 
    # initial_franchise_fee = 
    # initial_investment_detailed = 
    # net_worth_requirement = 
    # cash_requirement = 
    # royalty_fee = 
    # ad_royalty_fee = 
    # term_of_agreement = 
    # is_franchise_term_renewable = 
    # financing_options = 
    # on_the_job_training = 
    # classroom_training =
    # additional_training =
    # ongoing_support = 
    # marketing_support = 
    # is_absentee_ownership_allowed =
    # can_this_franchise_be_run_from_home_mobile_unit =
    # can_this_franchise_be_run_part_time = 
    # are_exclusive_territories_available = 

# https://www.entrepreneur.com/franchises/dunkin