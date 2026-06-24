from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

url = "https://www.ebay.com/b/Cell-Phones-Smartphones/9355/bn_320094"

service = webdriver.ChromeService(executable_path='C:\\Users\\DELL\\.wdm\\drivers\\chromedriver\\win64\\149.0.7827.155\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get(url)

phoneList=[]
phonesList = driver.find_elements(By.XPATH,"//ul[contains]")















