import requests, re
import pandas as pd
from bs4 import BeautifulSoup

urls = ["https://www.cadburygifting.in/", "https://www.isdi.in/summer-school/", "https://realpython.com/",
 "https://www.jamboreeindia.com/", "https://www.geeksforgeeks.org/", "https://mindworkzz.in/", "https://dailytechsuggest.com/"]
emails = []

for i in urls:
    URL = i
    flag = False
    # Make HTTP request
    page = requests.get(URL)

    # parse the webpage
    soup = BeautifulSoup(page.content, 'html.parser')

    # find all div tags
    divisions = soup.find_all('div')
    for element in divisions:
        # extract text from div tags
        str = element.text.strip()
        # check for email ids in text extracted
        email = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", str)
        if email:
            # if found, add the email id to list of emails
            # print(email) 
            flag = True
            emails.append(email)
            break

    if (flag == False):
        emails.append("None")

table = {
    "Website" : urls,
    "Email Ids" : emails
}

dataframe = pd.DataFrame(table)
print('\n', dataframe)
print('\n')
//"CHECK ON PULL"





