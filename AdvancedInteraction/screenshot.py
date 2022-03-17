# screen shot 하는 이유는 버그 증거 수집

import time
import unittest
from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class ScreenshotTest(unittest.TestCase):
    def setUp(self):
        baseUrl = "http://automationpractice.com/index.php"
        s = Service("D:\selenium\drivers\chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)
        self.driver.implicitly_wait(30)
        # self.driver.maximize_window()
        self.driver.get(baseUrl)

    def test_screenshot_login(self):
        self.driver.find_element(By.LINK_TEXT, 'Sign in').click()
        self.driver.find_element(By.ID, 'email').send_keys("test@test.com")
        self.driver.find_element(By.ID, 'passwd').send_keys("test1122")
        self.driver.find_element(By.ID, 'SubmitLogin').click()

        self.takeScreenshot()

    def takeScreenshot(self):
        directory = "D:\\selenium\\AdvancedInteraction\\screenshot\\"
        fileName = str(round(time.time() * 1000)) + ".png"
        directory_file = directory + fileName

        try:
            self.driver.save_screenshot(directory_file)
            print("Screenshot saved to directory --> :: " + directory_file)
        except NotADirectoryError:
            print("Not a directory issue")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
