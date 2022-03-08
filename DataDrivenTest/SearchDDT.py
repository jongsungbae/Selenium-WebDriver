import unittest

from ddt import ddt, data, unpack
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@ddt
class SearchDDT(unittest.TestCase):
    def setUp(self):
        baseUrl = "http://magento-demo.lexiconn.com/"
        s = Service("D:\selenium\drivers\chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get(baseUrl)

    # specify test data using @data decorator
    @data(('phones', 1), ('music', 5))
    @unpack
    def test_search(self, search_value, expected_count):
        # get the search textbox
        search_field = self.driver.find_element(By.NAME, 'q')
        search_field.clear()

        # enter search keyword and submit
        # use search_value argument to pass data
        search_field.send_keys(search_value)
        search_field.submit()

        # get all the anchor elements which have product names
        products = self.driver.find_elements(By.XPATH, "//h2[@class='product-name']/a")

        # check count of products in result
        self.assertEqual(expected_count, len(products))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


