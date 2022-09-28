import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

from parse_url import parse_url
from parse import parse

job_name ="Data"
job_name2="Science"
page_num = 1

url = "https://www.work.ua/ru/jobs-{}+{}/?page={}" \
    .format(job_name, job_name2, page_num)

if __name__ == '__main__':
    data_url = parse_url(url)
    print(data_url)
    for url in data_url:
        print(url)
        data = parse(url)

        df = pd.DataFrame(data)
        df.to_csv(r'test.csv',  mode='a', header=False, index=False)

