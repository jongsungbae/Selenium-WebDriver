import unittest
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By


class SearchTests(unittest.TestCase):
    def setUp(self):
        # create a new chrome session
        self.driver = webdriver.Chrome("D:\selenium\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # navigate to the application home page
        self.driver.get("http://automationpractice.com/index.php")

    def test_search_bycategory(self):
        # get the search textbox
        self.search_field = self.driver.find_element(By.NAME, "search_query")
        self.search_field.clear()

        # enter search keyword and submit
        self.search_field.send_keys("dress")
        self.search_field.submit()

        # get all the anchor elements which have product names
        # displayed currently on result page using
        # find_element by Xpath method
        products = self.driver.find_elements(By.XPATH, "//*[@id='center_column']/ul/li")
        self.assertEqual(7, len(products))

    def tearDown(self):
        # close the browser window
        self.driver.quit()

if __name__=='__main__':
    unittest.main()