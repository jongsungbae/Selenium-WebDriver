import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class WaitingTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        baseUrl = "http://magento-demo.lexiconn.com/"
        s = Service("D:\selenium\drivers\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=s)
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get(baseUrl)

    def test_a_create_new_customer(self):
        # click on Log In link to open login page
        self.driver.find_element(By.LINK_TEXT, 'ACCOUNT').click()

        # wait for My Account link in Menu
        my_account = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, 'My Account')))
        my_account.click()

        # get the create button
        create_account_button = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, 'CREATE AN ACCOUNT')))
        create_account_button.click()

        WebDriverWait(self.driver, 10).until(expected_conditions.title_contains("Create New Customer"))

    def test_b_compare_product(self):
        # get the search field and submit the keyword
        search_field = self.driver.find_element(By.NAME, 'q')
        search_field.clear()
        search_field.send_keys('phone')
        search_field.submit()

        # click the compare link
        self.driver.find_element(By.LINK_TEXT, 'Add to Compare').click()

        # wait for Clear All link to be visible
        clear_all_link = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, 'Clear All')))

        # click on Clear All link
        clear_all_link.click()

        # wait for the alert to present
        alert = WebDriverWait(self.driver, 10).until(expected_conditions.alert_is_present())

        # get the text from alert
        alert_text = alert.text

        self.assertEqual('Are you sure you would like to remove all products from your comparison?', alert_text)
        alert.accept()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()




