from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv
URL = ''https://www.alibaba.com/trade/search?spm=a2700.product_home_newuser.header.132.2ce267afSeLPmg&SearchText=Auto+Accessories&indexArea=product_en&search_cource_scene=pc_home_product_category&has4Tab=true&tab=all''

service = webdriver.ChromeService(executable_path='C:\\Users\\DELL\\.wdm\\drivers\\chromedriver\\win64\\149.0.7827.155\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get(URL)
phone_l = []
phonediv = driver.find_elements(By.XPATH,"//ul[contains(@class, 'test-center')]")
for p in range(len(phonediv) -1):
    phone = {}
    phone['img'] = phonediv[p+1].find_element(By.TAG_NAME, 'img')
    phone_l.append(phone)
file_name = 'Web_Scraped/cellphones_smartphones_alibaba.csv'
with open (file_name,'w', newline='') as f:
    w = csv.DictWriter(f, ['image'])
    w.writeheader()
    for phone in phone_l:
        w.writeheader(phone)
driver.close()