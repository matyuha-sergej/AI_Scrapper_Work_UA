import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

job_name ="Data"
job_name2="Science"
page_num = 1

url = "https://www.work.ua/ru/jobs-{}+{}/?page={}" \
    .format(job_name, job_name2, page_num)



if __name__ == '__main__':
    print(url)

