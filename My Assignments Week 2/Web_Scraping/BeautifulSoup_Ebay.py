import requests
from bs4 import BeautifulSoup
import csv


with open('C:\\Users\\DELL\\OneDrive\\Documents\\GitHub\\My-Ai-Course-Bin\\My Assignments Week 2\\Website\\eBay.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html5lib')

phones = []

table =  soup.find('ul', attrs={'class': 'brwrvr__item-results brwrvr__item-results--list'}) 

for row in table.find_all('li', attrs={'class': 'brwrvr__item-card'}):
    phone = {}
    phone['title'] = row.find('h3', attrs={'class': 'textual-display bsig__title__text'}).text
    phone['price'] = row.find('span', attrs={'class': "textual-display bsig__price bsig__price--displayprice"}).text
    phone['img']   = row.img['src']
    phone['url']   = row.a['href']
    phones.append(phone)

filename = 'Web_Scraped/cellphones_smartphones_ebay.csv'
with open(filename, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f,['title','img','url','price'])
    w.writeheader()
    for phone in phones:
        w.writerow(phone)