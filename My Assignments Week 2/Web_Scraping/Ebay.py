import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.ebay.com/b/Cell-Phones-Smartphones/9355/bn_320094"
a = requests.get(URL)

soup = BeautifulSoup(a.content, 'html5lib')

phones = []

table = soup.find('ul',attrs={'class':'brwrvr__item-results brwrvr__item-results--list'})
print(soup.prettify()[:2000])

for row in table.find_all('div',attrs={'class':'brwrvr_item-card_body'}):
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