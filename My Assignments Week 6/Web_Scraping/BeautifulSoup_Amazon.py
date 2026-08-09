import requests
from bs4 import BeautifulSoup
import csv

with open('C:\\Users\\DELL\\OneDrive\\Documents\\GitHub\\My-Ai-Course-Bin\\My Assignments Week 6\\Website\\Amazon.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html5lib')

phones1 = []

table1 = soup.find('div',attrs={ 'class':'a-section a-spacing-medium _octopus-search-result-card_style_apbSearchResultsContainer__bCqjb'})

for row in table1.find_all('div', attrs={"class":'_octopus-search-result-card_style_apbSearchResultItem__2-mx4'}):
    phone1 = {}
    phone1 ['title']= row.find('h2').text
    phone1['price'] = row.find('span', attrs={'class':'a-price'}).text if row.find('span', attrs={'class':'a-price'}) else "No Price"
    phone1['img']   = row.img['src']
    phone1['rate'] = row.find('div', attrs={'class': "a-row a-size-small"}).text
    phones1.append(phone1)
    
filename = 'My Assignments Week 6/Web_Scraped/BS4_appliances_amazon.csv'

with open (filename,'w', newline='', encoding='utf-8-sig') as f:
    w = csv.DictWriter(f,['title','price','img','rate'])
    w.writeheader()
    for phone1 in phones1:
        w.writerow(phone1)






