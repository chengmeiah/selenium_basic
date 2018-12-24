from selenium import webdriver
import time
driver = webdriver.Chrome()
def openbaidu():
    driver.get("http://www.baidu.com")
    driver.find_element_by_id('kw').send_keys('helloword')
    driver.save_screenshot('./baidu.png')
def openbeing():
    driver.get('https://cn.bing.com')
    driver.find_element_by_id("sb_form_q").send_keys('helloword')
    driver.save_screenshot("./bing.png")

openbaidu()
openbeing()
time.sleep(3)
 driver.quit()



from selenium import webdriver
import time
driver = webdriver.Chrome()
def aaa(url,selector,keyword):
    driver.get(url)
    if selector == 'kw':
        driver.find_element_by_id("kw").send_keys("keyword")
        driver.save_screenshot('./baidu.png')
    elif selector == "sb_form_q":
        driver.find_element_by_id("sb_form_q").send_keys('keyword')
        driver.save_screenshot('./bing.png')
aaa('http://www.baidu.com','kw','helloworld')
aaa('http://cn.bing.com','sb_form_q','helloworld')
time.sleep(3)
driver.quit()

