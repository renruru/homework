from selenium import webdriver
import time
dre = webdriver.Chrome()

dre.get("http://pawork.lenovo.com/oa/index.php")
# dre.find_element_by_css_selector('#kw').send_keys('hello world!')
# dre.find_element_by_xpath('//*[@id="kw"]').send_keys('hello world')
dre.find_element_by_css_selector('#userName').send_keys('renruru')
dre.find_element_by_css_selector('#password').send_keys('201515')
time.sleep(3)
#dre.find_element_by_css_selector('#login').find_element_by_id('login').find_element_by_class_name('btn btn-primary btn-block btn-flat').click
dre.find_element_by_id('login').click
# dre.find_element_by_css_selector('#login').click

dre.find_element_by_css_selector('body > div > aside > section > ul > li.treeview.list4_1.list4_2.list4_3.list4_4.list4_5.list4_6_1.list4_6_2.list4_7 > a > span').click

# <button id="login" type="submit" class="btn btn-primary btn-block btn-flat">登录</button>

# time.sleep(3)
# dre.quit()
# print(help(webdriver.Chrome()))