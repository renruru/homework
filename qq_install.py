from selenium import webdriver
browser=webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
browser.get('http://www.baidu.com/')
input1=browser.find_element_by_css_selector('[type="text"]').send_keys('QQ')
button1=browser.find_element_by_css_selector('[type="submit"]').click()