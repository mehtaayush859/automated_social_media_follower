from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import time

path = Service("chrome_driver\chromedriver.exe")
driver = webdriver.Chrome(service=path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")


"""By css element selector an get clicked"""
no = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# no.click()
# print(no.text)

"""By link element by text an get clicked"""
article_link = driver.find_element(By.LINK_TEXT, "View history")
# article_link.click()

"""Send keys or type something in input type then use this"""
search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)


time.sleep(10)
driver.close()