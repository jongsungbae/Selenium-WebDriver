import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class ElementTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # create chrome session
        cls.driver = webdriver.Chrome("D:\selenium\chromedriver.exe")
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get("http://automationpractice.com/index.php")

    def test_search_field(self):
        # check search field exists on Home page
        self.assertTrue(self.is_element_present(By.NAME,"search_query"))

if __name__ == '__main__':
    unittest.main()