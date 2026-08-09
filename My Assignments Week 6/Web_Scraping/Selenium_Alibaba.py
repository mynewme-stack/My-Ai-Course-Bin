from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv
URL = 'https://www.alibaba.com/trade/search?spm=a2700.product_home_newuser.header.132.2ce267afSeLPmg&SearchText=Auto+Accessories&indexArea=product_en&search_cource_scene=pc_home_product_category&has4Tab=true&tab=all'

service = webdriver.ChromeService(executable_path='C:\\Users\\DELL\\.wdm\\drivers\\chromedriver\\win64\\149.0.7827.155\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(5)
driver.get(URL)
phone_l = []
phonediv = driver.find_elements(By.XPATH,"//div[contains(@class, 'searchx-offer-item')]")
for p in phonediv:
    phone = {}
    phone['title'] = p.find_element(By.XPATH, ".//h2[@class='searchx-product-e-title']").text
    phone['price'] = p.find_element(By.XPATH, ".//div[@class='searchx-product-price-price-main']").text
    phone['img'] = p.find_element(By.TAG_NAME, 'img').get_attribute('src')
    phone_l.append(phone)
file_name = 'My Assignments Week 6/Web_Scraped/Selenium_smartphones_alibaba.csv'
with open (file_name,'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, ['title','price','img'])
    w.writeheader()
    for phone in phone_l:
        w.writerow(phone)
driver.close()

# Note: The code has not been updated since month. 