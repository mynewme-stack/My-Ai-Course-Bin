from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

URL = "https://www.daraz.pk/catalog/?spm=a2a0e.tm80331704.cate_5.5.77cc5aa7fPImi7&q=Smart%20Phones&from=hp_categories&src=all_channel"

service = webdriver.ChromeService(executable_path='C:\\Users\\DELL\\.wdm\\drivers\\chromedriver\\win64\\149.0.7827.155\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get(URL)
phone_list = []
phone_div = driver.find_elements(By.XPATH,"//ul[contains(@class, 'text- center')]")
for p in range(len(phone_div)-1):
    phone = {}
    phone ['img'] = phone_div[p+1].find_element(By.TAG_NAME, 'img')
    phone_list.append(phone)
file_n = 'Web_Scraped/cellphones_smartphones_ebay.csv' 
with open (file_n, 'w', newline='') as f:
    w = csv.DictWriter(f,['image'])
    w.writeheader()
    for phone in phone_list:
        w.writeheader(phone)
driver.close()