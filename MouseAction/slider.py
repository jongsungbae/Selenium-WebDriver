import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class Slider(unittest.TestCase):
    def setUp(self):
        baseUrl = "https://jqueryui.com/slider/"
        s = Service("E:\selenium\drivers\chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get(baseUrl)

    def test_slider(self):
        self.driver.switch_to.frame(0)
        element = self.driver.find_element(By.XPATH, ".//div[@id='slider']//span")
        time.sleep(2)
        try:
            actions = ActionChains(self.driver)
            actions.drag_and_drop_by_offset(element, 100, 0).perform()
            print("success")
        except:
            print("Fail")



    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()