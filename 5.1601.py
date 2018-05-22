from selenium import webdriver
import time 

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

search_text = driver.find_element_by_id('kw')
search_text.send_keys('selenium')
search_text.submit()
time.sleep(3)
mubiao = driver.find_element_by_xpath('//*[@id="1"]/h3/a')
mubiao.click()
time.sleep(2)
wds = driver.window_handles
print(len(wds))
driver.switch_to_window(wds[1])
print(driver.find_element_by_xpath('//*[@id="header"]/h1/a').text)
print(driver.find_element_by_xpath('//*[@id="header"]/h1/a').get_attribute)
# print(driver.find_element_by_xpath('//*[@id="header"]/h1/a').size)
# print(driver.find_element_by_xpath('//*[@id="header"]/h1/a').is_displayed)

time.sleep(10)
# driver.quit()
