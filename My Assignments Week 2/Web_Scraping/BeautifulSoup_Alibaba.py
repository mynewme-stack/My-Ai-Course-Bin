import requests
from bs4 import BeautifulSoup
import csv

with open('C:\\Users\\DELL\\OneDrive\\Documents\\GitHub\\My-Ai-Course-Bin\\My Assignments Week 2\\Website\\Alibaba.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html5lib')

phones= []
table = soup.find('div', attrs={'id':'sse-fluent-offerlist'})
for row in table.find_all('div', attrs={'class':'fy26-product-card-wrapper'}):
    phone = {}
    phone['title'] = row.find('h2', attrs= {'class':'searchx-product-e-title'}).text
    phone['price'] = row.find('div', attrs={'class':'searchx-product-price-price-main'}).text
    phone['img']   = row.img['src']
    phone['url']   = row.a['href']
    phones.append(phone)
file_name = 'Web_Scraped/cellphones_smartphones_Alibaba.csv'
with open(file_name, 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.DictWriter(f, ['title','price','img','url'])
    w.writeheader()
    for phone in phones:
        w.writerow(phone)