import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.daraz.pk/catalog/?spm=a2a0e.tm80331704.cate_5.5.77cc5aa7fPImi7&q=Smart%20Phones&from=hp_categories&src=all_channel"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

phones = []

table = soup.find('', attrs={'':''})

for row in table.find_all('', attrs={'':''}):
    phone = {}
    phone['title'] = row.find()
    phones.append(phone)

filename = 'Web_Scraped/cellphones_smartphones_Daraz.csv'
with open (filename, 'w', newline='') as f:
    w= csv.DictWriter(f, ['title'])
    w.writeheader()
    for phone in phones:
        w.writeheader(phone)