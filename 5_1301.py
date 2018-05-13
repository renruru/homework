from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

driver.find_element_by_xpath('//*[@id="u1"]/a[7]').click()
time.sleep(5)
driver.find_element_by_id('TANGRAM__PSP_10__footerULoginBtn').click()
time.sleep(5)
driver.find_element_by_id('TANGRAM__PSP_10__userName').clear()
driver.find_element_by_id('TANGRAM__PSP_10__userName').send_keys("15001707527")
driver.find_element_by_id('TANGRAM__PSP_10__password').send_keys("r15001707527")
driver.find_element_by_id('TANGRAM__PSP_10__submit').click()
driver.find_element_by_css_selector('')
time.sleep(10)
driver.close()


# driver.get('http://118.31.19.120:3000/signin')
# driver.find_element_by_class_name('input-xlarge').find_element_by_id('name').send_keys('testuser13')
# # time.sleep(3)
# driver.find_element_by_id('pass').send_keys('123456')
# # time.sleep(3)
# driver.find_element_by_class_name('span-primary').click()
# time.sleep(5)
# driver.close()