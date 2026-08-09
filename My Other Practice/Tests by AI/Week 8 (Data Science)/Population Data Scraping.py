import requests
from bs4 import BeautifulSoup

with open('C:\\Users\\DELL\\OneDrive\\Documents\\GitHub\\Tests by AI\\My AI Tests\\Week 8 (Data Science)\\List of countries and dependencies by population (United Nations) - Wikipedia.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html5lib')

table = soup.find('table', attrs={'class':'wikitable sortable mw-datatable sticky-header static-row-numbers sort-under col1left col5left col6left jquery-tablesorter'})

for row in table.find_all('div', attrs={'class':'Bm3ON'}):
    listed = {}
    listed['countries'] = row.find('tr', attrs= {'id':'mw0v'}).text
    listed[''] = row.find('div', attrs={'class':'aBrP0'}).text
    listed
    listed['url']   = row.a['href']
    listed.append(listed)

filename = 'My Assignments Week 2/Web_Scraped/cellphones_smartphones_Daraz.csv'
with open (filename, 'w', newline='', encoding='utf-8-sig') as f:
    w= csv.DictWriter(f, ['title','price','img','url'])
    w.writeheader()
    for listed in table:
        w.writerow(listed)