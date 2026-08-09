import requests
from bs4 import BeautifulSoup

with open('C:\\Users\\DELL\\OneDrive\\Documents\\GitHub\\Tests by AI\\My AI Tests\\Week 8 (Data Science)\\List of countries and dependencies by population (United Nations) - Wikipedia.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html5lib')

table = soup.find('tbody', attrs={'id':'mwJg'})

for row in table.find_all('a', attrs={'class':'Bm3ON'}):
    phone = {}
    phone['title'] = row.find('div', attrs= {'class':'RfADt'}).text
    phone['price'] = row.find('div', attrs={'class':'aBrP0'}).text
    phone['img']   = row.img['src']
    phone['url']   = row.a['href']
    phones.append(phone)

filename = 'Population_Wiki.csv'
with open (filename, 'w', newline='', encoding='utf-8-sig') as f:
    w= csv.DictWriter(f, ['title','price','img','url'])
    w.writeheader()
    for phone in phones:
        w.writerow(phone)