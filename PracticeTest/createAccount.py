import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class CreateAccount(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        baseUrl = "http://magento-demo.lexiconn.com/"
        s = Service("D:\selenium\drivers\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=s)
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get(baseUrl)

    def test_a_move_account_page(self):
        #driver = self.driver
        self.driver.find_element(By.LINK_TEXT, "ACCOUNT").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.assertTrue(WebDriverWait(self.driver, 10).until(expected_conditions.title_is('Create New Customer Account')))

    def test_b_check_textField(self):
        first_name = self.driver.find_element(By.NAME, 'First Name')
        last_name = self.driver.find_element(By.NAME, 'Last Name')
        email = self.driver.find_element(By.NAME, 'email')
        password = self.driver.find_element(By.NAME, 'password')
        confirm_password = self.driver.find_element(By.NAME, 'confirmation')
        check_newsletter = self.driver.find_element(By.NAME, 'is_subscribed')
        back_button = self.driver.find_element(By.XPATH, '//*[@id="form-validate"]/div[2]/p/a')
        register_button = self.driver.find_element(By.XPATH, '//*[@id="form-validate"]/div[2]/button')

        # check all field are enabled
        self.assertTrue(
            first_name.is_enabled() and last_name.is_enabled() and email.is_enabled() and password.is_enabled()
            and confirm_password.is_enabled() and check_newsletter.is_enabled() and back_button.is_enabled()
            and register_button.is_enabled())

        # check maxlength and is_selected of check box
        self.assertEqual("255", first_name.get_attribute("maxlength"))
        self.assertEqual("255", last_name.get_attribute("maxlength"))
        self.assertFalse(check_newsletter.is_selected())














