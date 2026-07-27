import requests
from bs4 import BeautifulSoup

with open('C:\\Users\\DELL\\OneDrive\\Documents\\GitHub\\Tests by AI\\My AI Tests\\Week 8 (Data Science)\\List of countries and dependencies by population (United Nations) - Wikipedia.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html5lib')

