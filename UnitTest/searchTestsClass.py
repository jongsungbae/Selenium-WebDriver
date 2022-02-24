import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class SearchTestsClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # create a new chrome session
        cls.driver = webdriver.Chrome("D:\selenium\chromedriver.exe")
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        # navigate to the application home page
        cls.driver.get("http://automationpractice.com/index.php")

    def test_search_by_category(self):
        # get the search textbox
        self.search_field = self.driver.find_element(By.NAME, "search_query")
        self.search_field.clear()

        # enter search keyword and submit
        self.search_field.send_keys("dress")
        self.search_field.submit()
        time.sleep(3)

        # get all the anchor elements which have product names
        # displayed currently on result page using
        # find_element by Xpath method
        products = self.driver.find_elements(By.XPATH, "//*[@id='center_column']/ul/li")
        self.assertEqual(7, len(products))

    def test_search_by_name(self):
        # get the search textbox
        self.search_field = self.driver.find_element(By.NAME, "search_query")
        self.search_field.clear()

        # enter search keyword and submit
        self.search_field.send_keys("shirts")
        self.search_field.submit()
        time.sleep(3)

        # get all the anchor elements which have product names
        # displayed currently on result page using
        # find_element by Xpath method
        products = self.driver.find_elements(By.XPATH, "//*[@id='center_column']/ul/li")
        self.assertEqual(1, len(products))

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()

if __name__=='__main__':
    unittest.main()