from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
class BaiDuSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_baidu_search(self):
        driver = self.driver
        driver.get('https://www.baidu.com')
        driver.find_element_by_id('kw').send_keys('hellloworld')
        driver.find_element_by_id('kw').send_keys(Keys.ENTER)
    def test_bing_search(self):
        driver = self.driver
        driver.get('http://cn.bing.com')
        driver.find_element_by_id('sb_form_q').send_keys('hellloworld')
        driver.find_element_by_id('sb_form_q').send_keys(Keys.ENTER)
    def tearDown(self):
        self.driver.quit()
if __name__=="__main__":
    unittest.main()

