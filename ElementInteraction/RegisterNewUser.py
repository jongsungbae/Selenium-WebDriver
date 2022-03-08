import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class RegisterNewUser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        baseUrl = "http://magento-demo.lexiconn.com/"
        s = Service("D:\selenium\drivers\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=s)
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get(baseUrl)

    def test_move_to_register(self):
        # move to Login page
        self.driver.find_element(By.LINK_TEXT, 'Log In').click()

        # get the create account btn and check enable
        create_account_btn = self.driver.find_element(By.XPATH, '//*[@id="login-form"]/div/div[1]/div[2]/a')
        self.assertTrue(create_account_btn.is_displayed() and create_account_btn.is_enabled())

        # move to create account page
        create_account_btn.click()
        # check title
        driver = self.driver
        self.assertEqual("Create New Customer Account", driver.title)

    def test_regester_field(self):
        # get all the fields
        first_name = self.driver.find_element(By.ID, 'firstname')
        last_name = self.driver.find_element(By.ID, 'lastname')
        email_address = self.driver.find_element(By.ID, 'email_address')
        password = self.driver.find_element(By.ID, 'password')
        confirm_password = self.driver.find_element(By.ID, 'confirmation')
        news_letter_subscription = self.driver.find_element(By.ID, 'is_subscribed')
        submit_button = self.driver.find_element(By.XPATH, '//*[@id="form-validate"]/div[2]/button')

        # check maxlength or first name and last name
        self.assertEqual('255', first_name.get_attribute('maxlength'))
        self.assertEqual('255', last_name.get_attribute('maxlength'))

        # check all fields are enabled
        self.assertTrue(
            first_name.is_enabled() and last_name.is_enabled() and email_address.is_enabled() and password.is_enabled() and
            confirm_password.is_enabled() and news_letter_subscription.is_enabled() and submit_button.is_enabled())

        # check Newsletter is unchecked
        self.assertFalse(news_letter_subscription.is_selected())

        # fill out all the fields
        first_name.send_keys('ftest')
        last_name.send_keys('ltest')
        email_address.send_keys('test@test.com')
        password.send_keys('test')
        confirm_password.send_keys('test')
        news_letter_subscription.click()

        # click submit button
        submit_button.click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()









