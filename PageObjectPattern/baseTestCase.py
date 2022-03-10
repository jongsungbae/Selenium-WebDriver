import unittest
from selenium import  webdriver
from selenium.webdriver.chrome.service import Service

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        baseUrl = "http://magento-demo.lexiconn.com/"
        s = Service("D:\selenium\drivers\chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get(baseUrl)

    def tearDown(self):
        self.driver.quit()

