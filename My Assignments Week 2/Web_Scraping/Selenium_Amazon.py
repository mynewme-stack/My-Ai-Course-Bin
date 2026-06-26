from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

URL = 'https://www.amazon.com/b?_encoding=UTF8&node=21217035011&ref_=cct_cg_SHnav2_2a1&pf_rd_p=12b44fc7-b592-4f55-b8d7-32c20b211ef1&pf_rd_r=9Z4KFSRNJF7N2MG3RRFC'

service = webdriver.ChromeService(executable_path='C:\\Users\\DELL\\.wdm\\drivers\\chromedriver\\win64\\149.0.7827.155\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get(URL)
phoneList = []
phonediv = driver.find_elements(By.XPATH, "//ul[contains(@class, 'text- center')]")
for p in range(len(phonediv) -1):
    phone = {}
    phone['img'] = phonediv[p+1].find_element(By.TAG_NAME,'img')
    phoneList.append(phone)
file_name = 'Web_Scraped/selenium_cellphones_smartphones_amazon.csv'
with open (file_name, 'w', newline='') as f:
    w= csv.DictWriter(f,['image'])
    w.writeheader()
    for phone in phoneList:
        w.writeheader(phone)
driver.close()