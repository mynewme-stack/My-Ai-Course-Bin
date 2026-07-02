from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

URL = "https://www.daraz.pk/catalog/?spm=a2a0e.tm80331704.cate_5.5.77cc5aa7fPImi7&q=Smart%20Phones&from=hp_categories&src=all_channel"

service = webdriver.ChromeService(executable_path='C:\\Users\\DELL\\.wdm\\drivers\\chromedriver\\win64\\149.0.7827.155\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(20)
driver.get(URL)
phone_list = []
phone_div = driver.find_elements(By.XPATH, "//div[@data-qa-locator='product-item']")
for p in phone_div:
    phone = {}
    phone['title'] = p.find_element(By.XPATH, ".//div[@class='RfADt']").text
    phone['price'] = p.find_element(By.XPATH, ".//div[@class='aBrP0']").text
    phone['img'] = p.find_element(By.TAG_NAME, "img").get_attribute('src')
   
    phone_list.append(phone)
file_n = 'Web_Scraped/selenium_cellphones_smartphones_daraz.csv' 
with open (file_n, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f,['title','price','img'])
    w.writeheader()
    for phone in phone_list:
        w.writerow(phone)
driver.close()