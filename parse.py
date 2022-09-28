import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

def parse(url):
    result_list = {'title': [], 'company': [], 'about': [], 'location': [], 'date': []}


    r = requests.get(url)
    soup = bs(r.text, "html.parser")
    result_list['title'].append(soup.find("h1", {"id": "h1-name", "class": "add-top-sm"}).text)
    result = soup.find("div", {"class":"card wordwrap"}).find_all("p", class_="text-indent text-muted add-top-sm")
    for item in result:
        if item.a is not None:
            result_list['company'].append(item.a.get("title"))
    result_list['about'].append(soup.find("div" , class_= "card wordwrap").find("div", {"id": "job-description"}).text)
    result_list['location'].append(soup.find("p", class_="text-indent add-top-sm").text)
    result_list['date'].append(soup.find("p", class_="cut-bottom-print flex flex-wrap flex-align-center").text)
    print(result_list)
    print("=======================================================================================")
    return result_list