from bs4 import BeautifulSoup
import time
import requests
import shutil
import os 

url = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=")
soup = BeautifulSoup(url.content,"lxml")

try:
    shutil.rmtree("jobs")
except:
    pass
os.mkdir("jobs")

def list_jobs():

    unwanted_skills = input("Enter a skill that you dont want to list (etc: javascript):\n>")
    print("\n Filtering the jobs...")

    jobs = soup.find_all("li",class_="clearfix job-bx wht-shd-bx")
    for index,job in enumerate(jobs):

        companyName = job.find("h3",class_="joblist-comp-name").text.strip()
        skills = job.find("span", class_="srp-skills").text.strip().replace(" ","")
        link = job.find("header").h2.a['href']

        if unwanted_skills == "":
            unwanted_skills = "----"

        if unwanted_skills not in skills:

            with open(f"jobs/job{index+1}.txt",'w') as f:
                if '(More Jobs)' not in companyName:

                    f.write(f"Company Name: {companyName}\n")
                    f.write(f"Skills: {skills}\n")
                    f.write(f"Link: {link}")
                else:

                    companyName = companyName.split()
                    companyName.pop(-1)
                    companyName.pop(-1)
                    companyName = " ".join(companyName)
                    f.write(f"Company Name: {companyName}\n")
                    f.write(f"Skills: {skills}\n")
                    f.write(f"Link: {link}")

            print(f"File saved: {index+1}")

if __name__ == '__main__':
    list_jobs()
    input("\npress enter to exit...")

# Purpose of program:
# Its basically gathering data of all python jobs in TimesJobs.com and writing them to txt files
# and you can specify a skill that you dont want to list