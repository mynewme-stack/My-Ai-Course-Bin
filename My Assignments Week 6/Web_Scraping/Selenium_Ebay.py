from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

URL = "https://www.ebay.com/b/Cell-Phones-Smartphones/9355/bn_320094"

service = webdriver.ChromeService(executable_path='C:\\Users\\DELL\\.wdm\\drivers\\chromedriver\\win64\\149.0.7827.155\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(5)
driver.get(URL)

phoneList=[]
phonesDiv = driver.find_elements(By.XPATH,"//li[contains(@class,'brwrvr__item-card')]")
for p in phonesDiv:
    phone = {}
    phone['title'] = p.find_element(By.XPATH, ".//h3[@class='textual-display bsig__title__text']").text
    phone['price'] = p.find_element(By.XPATH, ".//span[@class='textual-display bsig__price bsig__price--displayprice']").text
    phone['img'] = p.find_element(By.TAG_NAME, "img").get_attribute('src')
   
    phoneList.append(phone)
file_name = 'My Assignments Week 6/Web_Scraped/selenium_smartphones_ebay.csv' 
with open (file_name, 'w', newline='', encoding='utf-8') as f:
    w= csv.DictWriter(f,['title','price','img'])
    w.writeheader()
    for phone in phoneList:
        w.writerow(phone)
driver.close()


# Note: The code has not been updated since month. 