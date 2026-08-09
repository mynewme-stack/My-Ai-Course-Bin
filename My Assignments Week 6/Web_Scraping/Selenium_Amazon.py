from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv
import undetected_chromedriver as uc 
import os

URL = 'https://www.amazon.com/b?_encoding=UTF8&node=21217035011&ref_=cct_cg_SHnav2_2a1&pf_rd_p=12b44fc7-b592-4f55-b8d7-32c20b211ef1&pf_rd_r=9Z4KFSRNJF7N2MG3RRFC'

options = uc.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\Users\DELL\AppData\Local\Google\Chrome\ScrapingData")
options.add_argument("--profile-directory=Default")
driver = uc.Chrome(options=options, use_subprocess=True, version_main=149)
driver.get(URL)
driver.implicitly_wait(10)
phoneList = []
phonediv = driver.find_elements(By.XPATH,  "//div[contains(@class, '_octopus-search-result-card_style_apbSearchResultItem')]")
for p in phonediv:
    phone = {}
    phone['title'] = p.find_element(By.TAG_NAME, "h2").text
    try:
        phone['price'] = p.find_element(By.XPATH, ".//span[@class='a-price']").text
    except:
        phone['price'] = "No Price"
    phone['img'] = p.find_element(By.TAG_NAME, 'img').get_attribute('src')
    phoneList.append(phone)
os.makedirs('Web_Scraped', exist_ok=True)  
file_name = 'My Assignments Week 6/Web_Scraped/selenium_appliances_amazon.csv'
with open (file_name, 'w', newline='', encoding='utf-8') as f:
    w= csv.DictWriter(f,['title','price','img'])
    w.writeheader()
    w.writerows(phoneList)
driver.quit()


# Note: The code has not been updated since month. 