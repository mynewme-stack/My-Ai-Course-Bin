import requests
from bs4 import BeautifulSoup
import csv

URL= 'https://www.amazon.com/b?_encoding=UTF8&node=21217035011&ref_=cct_cg_SHnav2_2a1&pf_rd_p=12b44fc7-b592-4f55-b8d7-32c20b211ef1&pf_rd_r=9Z4KFSRNJF7N2MG3RRFC'
b = requests.get(URL)

soup = BeautifulSoup(b.content, 'html5lib')

phones1 = []

table1 = soup.find('div', attrs={ 'class':"a-section a-spacing-medium _octopus-search-result-card_style_apbSearchResultsContainer__bCqjb"}) 

for row in table1.find_all('div', attrs={"class":"a-declarative"}):
    phone1 = {}
    phone1 ['img']= row.img['src']
    phones1.append(phone1)
filename = 'Week6/amazon_phones.csv'
with open (filename,'w', newline='') as f:
    w = csv.DictWriter(f,['img'])
    w.writeheader()
    for phone1 in phones1:
        w.writerow(phone1)






