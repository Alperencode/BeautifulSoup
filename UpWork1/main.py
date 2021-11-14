import contextlib
from bs4 import BeautifulSoup
import requests
import pandas as pd
masterlist = []

def Gather_info(pageNumber):
    url = f"https://www.albertaagsocieties.ca/agsocieties/page/{pageNumber}/"
    headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
    }
    url = requests.get(url, headers=headers)
    soup = BeautifulSoup(url.content,"lxml")
    sections = soup.find("ul", class_="geodir-category-list-view clearfix gridview_onehalf geodir-listing-posts geodir-gridview gridview_onehalf").li.next_siblings
    for section in sections:
        data_dict = {}
        with contextlib.suppress(TypeError):
            name = section.find("h2",class_="geodir-entry-title")
            general_phone = section.find("div",class_="geodir_post_meta geodir-field-phone")
            general_email = section.find("div",class_="geodir_post_meta geodir-field-general_email")
            facility_type = section.find("li",class_="geodir-fv-community-hall")
            paragraph =  section.find("div",class_="geodir_post_meta geodir-field-post_content")
            try:
                data_dict['Name'] = name.a.text
            except:
                data_dict['Name'] = "Not specified"
            try:        
                data_dict['Phone'] = general_phone.a.text
            except:
                data_dict['Phone'] = "Not specified"
            try:
                data_dict['Email'] = general_email.a.text
            except:
                data_dict['Email'] = "Not specified"
            try:
                data_dict['Facility Type'] = facility_type.text
            except:
                data_dict['Facility Type'] = "Not specified"
            try:
                data_dict['Descriptive Paragraph'] = paragraph.text
            except:
                data_dict['Descriptive Paragraph'] = "Not specified"
            masterlist.append(data_dict)
    print(f"Page Saved: {pageNumber}")

ExistingPageNumber = 15
for page in range(1,ExistingPageNumber+1):
    Gather_info(page)

df = pd.DataFrame(masterlist)
datatoexcel = pd.ExcelWriter(f"final.xlsx",engine='xlsxwriter')
df.to_excel(datatoexcel,index=False)
datatoexcel.save()