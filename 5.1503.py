from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://118.31.19.120:3000/signin')
driver.find_element_by_id('name').send_keys('testuser13')
driver.find_element_by_id('pass').send_keys('123456')
driver.find_element_by_id('pass').submit()
# driver.find_element_by_class_name('span-primary').click()
driver.find_element_by_class_name('span-success').click()
driver.find_element_by_id('tab-value').click()
driver.find_element_by_xpath('//*[@id="tab-value"]/option[2]').click()
driver.find_element_by_class_name('span9').send_keys('dhedehfjehfjfjkke')
time.sleep(3)
qqq = driver.find_element_by_xpath('//*[@id="create_topic_form"]/fieldset/div/div/div[2]/div[6]/div[1]/div/div/div/div[3]/pre')
ActionChains(driver).move_to_element(qqq).click().send_keys('ddddddddddddd').perform()

driver.find_element_by_xpath('//*[@id="create_topic_form"]/fieldset/div/div/div[4]/input').click()
time.sleep(5)

driver.find_element_by_xpath('//*[@id="manage_topic"]/a[2]/i').click()
alert = driver.switch_to_alert()
time.sleep(2)
print (alert.text) 
alert.accept()
time.sleep(10)
driver.quit()