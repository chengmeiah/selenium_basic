from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.baidu.com')
driver.find_element_by_id('kw').send_keys('helloworld')
driver.find_element_by_name('wd').send_keys('helloworld')
driver.find_element_by_class_name('s_ipt').send_keys('helloworld')
driver.find_element_by_css_selector('#kw').send_keys('helloworld')
diver.find_element_by_xpath('//*[@id="kw"]').send_keys('helloworld')
driver.find_element_by_link_text('新闻').click()
friver.find_element_by_partial_link_text('新').click()

        
