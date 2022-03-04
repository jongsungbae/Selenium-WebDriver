import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class AlertTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        baseUrl = "http://magento-demo.lexiconn.com/"
        s = Service("E:\selenium\drivers\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=s)
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get(baseUrl)

    def test_a_search_product(self):
        # get the search textbox
        search_field = self.driver.find_element(By.ID, 'search')
        search_field.click()

        # Enter keyword and submit
        search_field.send_keys('Phone')
        search_field.submit()

    def test_compare_products_add(self):
        # search_product = self.driver.find_element(By.LINK_TEXT, 'Madison Overear Headphones')
        self.driver.find_element(By.LINK_TEXT, 'Add to Compare').click()
        compare_product = self.driver.find_element(By.XPATH, '//*[@id="compare-items"]/li/p/a').text
        self.assertEqual('MADISON OVEREAR HEADPHONES', compare_product)

    def test_compare_products_removal_alert(self):
        # click on Remove all btn
        self.driver.find_element(By.LINK_TEXT, 'Clear All').click()
        # switch to the alert
        alert = self.driver.switch_to.alert
        # get the text from alert
        alert_text = alert.text
        # check alert text
        self.assertEqual('Are you sure you would like to remove all products from your comparison?', alert_text)
        # click on Cancle button
        alert.dismiss()
        self.driver.find_element(By.LINK_TEXT, 'Clear All').click()
        # click on OK button
        alert.accept()
        # check if compare products is empty
        emp_text = self.driver.find_element(By.XPATH, '//*[@id="top"]/body/div/div[2]/div[2]/div/div[3]/div/div[2]/p').text
        self.assertEqual("You have no items to compare.", emp_text)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()













