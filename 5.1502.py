from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')
driver.maximize_window() 
# eless = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,"mnav")))
eless = driver.find_element_by_class_name('mnav')
print(eless.text)
driver.quit()