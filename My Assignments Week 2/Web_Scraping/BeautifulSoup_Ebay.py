import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.ebay.com/b/Cell-Phones-Smartphones/9355/bn_320094"
a = requests.get(URL)

soup = BeautifulSoup(a.content, 'html5lib')
 
phones = []

table = soup.find('ul',attrs={'class':"brwrvr_item-results brwrvr_item-results--list"})

for row in table.find_all('li',attrs={'class':"brwrvr item-card brwrvr item-card--1 brwrvr item-card--list"}):
    phone = {}
    phone['title'] = row.find('span', attrs={'class':'bsig_title'}).text
    phone['price'] = row.find('span', attrs={'class': 'bsig_price'}).text
    phone['img']   = row.img['src']
    phone['url']   = row.a['href']
    phones.append(phone)

filename = 'Web_Scraped/cellphones_smartphones_ebay.csv'
with open (filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['title','img','url','price'])
    w.writeheader()
    for phone in phones:
        w.writerow(phone)