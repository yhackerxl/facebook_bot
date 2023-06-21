from selenium import webdriver
from selenium.webdriver.common.by import By
import time
b = webdriver.Chrome()
b.get("https://www.facebook.com")

email = b.find_element(By.ID,"email")
email.send_keys("kennedynnko@gmail.com")

p = b.find_element(By.ID,"pass")
p.send_keys("")

p.submit()
time.sleep(300)