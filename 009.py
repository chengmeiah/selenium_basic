import unittest
from selenium import webdriver

class Cnode(unittest.TestCase):
    def setUp(self):
        self.url = 'http://39.107.96.138:3000/'
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
    def test_register(self):
        driver = self.driver
        driver.find_element_by_css_selector('a[href="/signup"]').click()
        driver.find_element_by_id('loginname').send_keys('lisan')
        driver.find_element_by_id('pass').send_keys('123456')
        driver.find_element_by_id('re_pass').send_keys('123456')
        driver.find_element_by_id('email').send_keys('chengmei@163.com')
        driver.find_element_by_css_selector('#signup_form > div.form-actions > input').click()

    def test_login(self):
        driver = self.driver
        driver.find_element_by_css_selector('a[href="/signin"]').click()
        driver.find_element_by_id('name').send_keys('lisan')
        driver.find_element_by_id('pass').send_keys('123456')
        driver.find_element_by_css_selector('#signin_form > div.form-actions > input').click()
        pass
    def tearDown(self):
        self.driver.save_screenshot('./01.png')
        self.driver.quit()
if __name__ =="__main__":
    unittest.main()


