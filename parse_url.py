import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

def parse_url(url):
    result_list = []
    data = []
    r = requests.get(url)
    soup = bs(r.text, "html.parser")
    result = soup.find("div", {"id":"pjax-job-list"}).find_all("h2")
    old_url = pd.read_csv("url.csv")
    for item in result:
        if item.a is not None:
           data.append(item.a.get("href"))

    new_url = pd.DataFrame(data)
    new_url = new_url.loc[~new_url[0].isin(old_url['0'])]

    for i in new_url[0]:
        result_list.append("https://www.work.ua"+str(i))

    new_url.to_csv(r'url.csv', mode='a', index=False)
    return result_list