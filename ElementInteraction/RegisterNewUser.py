import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class RegisterNewUser(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        baseUrl = "https://www.phptravels.net/"
        s = Service("E:\selenium\drivers\chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get(baseUrl)

    def test_move_to_signUp(self):
        # click on sign up btn
        self.driver.find_element(By.LINK_TEXT, 'Signup').click()

        # check the title
        self.assertTrue("Signup - PHPTRAVELS", self.driver.title)

    def test_signUp_page(self):
        # get all the fields from create an Account form
        first_name = self.driver.find_element(By.NAME, 'first_name')
        last_name = self.driver.find_element(By.NAME, 'last_name')
        phone = self.driver.find_element(By.NAME, 'phone')
        email = self.driver.find_element(By.NAME, 'email')
        password = self.driver.find_element(By.NAME, 'password')
        drop_menu = self.driver.find_element(By.ID, 'select2-account_type-container')
        submit_button = self.driver.find_element(By.XPATH,'//*[@id="fadein"]/div[1]/div/div[2]/div[2]/div/form/div[7]/button')

        # check all fields are enabled
        self.assertTrue(first_name.is_enabled() and last_name.is_enabled() and phone.is_enabled() and email.is_enabled()
                        and password.is_enabled() and drop_menu.is_enabled() and submit_button.is_enabled())

        # fill out all the fields
        first_name.send_keys("test")
        last_name.send_keys("user1")
        phone.send_keys("123-456-7894")
        email.send_keys("test@test.com")
        password.send_keys("test1234")

        # submit button click
        submit_button.click()
        time.sleep(5)

        # move to login page
        self.assertTrue("Login - PHPTRAVELS", self.driver.title)

        @classmethod
        def tearDownClass(cls):
            self.driver.quit()

if __name__ == '__main__':
    unittest.main()







