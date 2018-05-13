from selenium import webdriver
import time

drive = webdriver.Chrome()
drive.get('https://www.baidu.com')
eles = drive.find_elements_by_class_name('mnav')
for x in eles:
    print(x.text)
# drive.find_element_by_css_selector('#kw').send_keys("解脱")
time.sleep(3)
drive.find_element_by_class_name('soutu-btn').click()
drive.find_element_by_class_name('upload-pic').send_keys("C:\\Users\\Administrator.W7-201607191031\\Desktop\\b\\2.jpg")
time.sleep(10)
drive.close()