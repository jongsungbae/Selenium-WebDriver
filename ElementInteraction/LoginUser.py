import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class LoginUser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        baseUrl = "https://www.phptravels.net/"
        s = Service("E:\selenium\drivers\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=s)
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get(baseUrl)

    def test_Login_page_title_check(self):
        # click on Login Btn
        self.driver.find_element(By.LINK_TEXT, 'Login').click()

        # check the title
        self.assertTrue(("Login - PHPTRAVELS"), self.driver.title)

    def test_login_page_check(self):
        login_text = self.driver.find_element(By.XPATH, '//*[@id="fadein"]/div[1]/div/div[2]/div[1]/div/p')
        email = self.driver.find_element(By.NAME, 'email')
        password = self.driver.find_element(By.NAME, 'password')
        checkbox = self.driver.find_element(By.ID, 'rememberchb')
        loginBtn = self.driver.find_element(By.XPATH, '//*[@id="fadein"]/div[1]/div/div[2]/div[2]/div/form/div[3]/button')

        # check the field
        self.assertTrue("Please enter your account credentials below", login_text.text)
        self.assertTrue("Email", email.get_attribute('placeholder'))
        self.assertTrue("Password", password.get_attribute('placeholder'))
        self.assertFalse(checkbox.is_selected())

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()