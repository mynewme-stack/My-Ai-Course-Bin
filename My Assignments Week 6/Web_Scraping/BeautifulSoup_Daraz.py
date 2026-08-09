import requests
from bs4 import BeautifulSoup
import csv


with open('C:\\Users\\DELL\\OneDrive\\Documents\\GitHub\\My-Ai-Course-Bin\\My Assignments Week 6\\Website\\Daraz.pk.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html5lib')

phones = []

table = soup.find('div', attrs={'id':'root'})

for row in table.find_all('div', attrs={'class':'Bm3ON'}):
    phone = {}
    phone['title'] = row.find('div', attrs= {'class':'RfADt'}).text
    phone['price'] = row.find('div', attrs={'class':'aBrP0'}).text
    phone['img']   = row.img['src']
    phone['url']   = row.a['href']
    phones.append(phone)

filename = 'My Assignments Week 6/Web_Scraped/BS4_smartphones_Daraz.csv'
with open (filename, 'w', newline='', encoding='utf-8-sig') as f:
    w= csv.DictWriter(f, ['title','price','img','url'])
    w.writeheader()
    for phone in phones:
        w.writerow(phone)