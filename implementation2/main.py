from bs4 import BeautifulSoup
import requests
url = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=")


soup = BeautifulSoup(url.content,"lxml")

jobs = soup.find_all("li",class_="clearfix job-bx wht-shd-bx")

for job in jobs:
    companyName = job.find("h3",class_="joblist-comp-name").text.strip()
    skills = job.find("span", class_="srp-skills").text.strip().replace(" ","")
    print(f"Company Name: {companyName}")
    print(f"Skills: {skills}")
    print("")