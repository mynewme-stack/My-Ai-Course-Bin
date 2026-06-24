import requests
from bs4 import BeautifulSoup
import csv

URL= 'https://www.alibaba.com/trade/search?spm=a2700.product_home_newuser.header.132.2ce267afSeLPmg&SearchText=Auto+Accessories&indexArea=product_en&search_cource_scene=pc_home_product_category&has4Tab=true&tab=all'
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')
phones= []
table = BeautifulSoup.find('', attrs={'':''})
for row in table.find_all('', attrs={'',''}):
    phone = {}
    phone['title'] = row.find()
    phones.append(phone)
file_name = 'Web_Scraped/cellphones_smartphones_Alibaba.csv'
with open(file_name, 'w', newline='') as f:
    w = csv.DictWriter(f, [ 'title'])
    w.writeheader()
    for phone in phones:
        w.writeheader(phone)