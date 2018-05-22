from selenium import webdriver
from os import path
import time

d = path.dirname(__file__)
xinwen = path.join(d,'xinwen.jpg')
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

driver.maximize_window()
driver.find_element_by_link_text("新闻").click()
# driver.save_screenshot(xinwen)
print('title:======================================================== ',driver.title)
print('url: ===================================================================',driver.current_url)
# print('source：========================================================================',driver.page_source)
time.sleep(3)
driver.quit()