import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class HomePageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("D:\selenium\chromedriver.exe")
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get("http://automationpractice.com/index.php")

    def test_search_field(self):
        # check search field exists on Home page
        self.assertTrue(self.is_element_present(By.NAME,"search_query"))

    def test_search_cart(self):
        # check cart button exists
        self.assertTrue(self.is_element_present(By.XPATH,"//*[@id='header']/div[3]/div/div/div[3]/div/a"))

    def test_shopping_cart(self):
        # check the message when the cart is empty
        shopping_cart_btn = self.driver.find_element(By.XPATH,"//*[@id='header']/div[3]/div/div/div[3]/div/a")
        shopping_cart_btn.click()
        time.sleep(3)

        shopping_cart_status = self.driver.find_element(By.XPATH,"//*[@id='center_column']/p").text
        self.assertEqual("Your shopping cart is empty.", shopping_cart_status)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def is_element_present(self, how, what):
        """
        :param how: By locator type
        :param what: locator value
        """
        try: self.driver.find_element(by=how, value= what)
        except NoSuchElementException as e: return False
        return True

if __name__ == '__main__':
    unittest.main()