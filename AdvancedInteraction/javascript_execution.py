import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class WaitingTest(unittest.TestCase):
    def setUp(self):
        # baseUrl = "https://courses.letskodeit.com/practice"
        s = Service("D:\selenium\drivers\chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)
        # javascript
        self.driver.execute_script("window.location ='https://courses.letskodeit.com/practice';")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def test_element(self):
        # element = self.driver.find_element(By.ID, "name")
        element = self.driver.execute_script("return document.getElementById('name');")
        element.send_keys("Test")
        time.sleep(5)





    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
