from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


path = Service("D:\Courses_tele\Practical\chrome_driver")
driver = webdriver.Chrome(service=path)


driver.get("https://www.python.org/")

# price = driver.find_element(By.CLASS_NAME, "cb-nws-intr")
# print(price.text)

dates = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
links = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')
events = {n:{'time':dates[n].text, 'name':links[n].text} for n in range(len(dates))}

print(events)

time.sleep(10)
driver.quit()

