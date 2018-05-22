from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
# time.sleep(10)
# driver.find_element_by_class_name('soutu-btn').click()
# driver.find_element_by_class_name('upload-pic').send_keys("C:\\Users\\mc\\Desktop\\a\\1.jpg")
list1 = driver.find_elements_by_class_name('mnav')
for x in list1:
    print(x.text)
time.sleep(3)
driver.quit()
