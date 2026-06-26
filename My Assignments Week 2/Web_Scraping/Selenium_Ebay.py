from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

URL = "https://www.ebay.com/b/Cell-Phones-Smartphones/9355/bn_320094"

service = webdriver.ChromeService(executable_path='C:\\Users\\DELL\\.wdm\\drivers\\chromedriver\\win64\\149.0.7827.155\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get(URL)

phoneList=[]
phonesDiv = driver.find_elements(By.XPATH,"//li[contains(@class,'brwrvr__item-card')]")
for p in range(len(phonesDiv) -1):
    phone = {}
    phone['img'] = phonesDiv[p+1].find_element(By.TAG_NAME,'img').get_attribute('src')
    phoneList.append(phone)
file_name = 'Web_Scraped/selenium_cellphones_smartphones_ebay.csv' 
with open (file_name, 'w', newline='') as f:
    w= csv.DictWriter(f,['img'])
    w.writeheader()
    for phone in phoneList:
        w.writerow(phone)
driver.close()