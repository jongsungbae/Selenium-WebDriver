import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class WaitingTest(unittest.TestCase):
    def setUp(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        s = Service("E:\selenium\drivers\chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get(baseUrl)

    def test_switch_to_window(self):
        # Find parent handle -> Main Window
        #parentHandle = self.driver.current_window_handle

        # Find open Window button and click it
        self.driver.find_element(By.ID, "openwindow").click()
        time.sleep(2)

        # Find all handles, there should two handles after clicking open window button
        handles = self.driver.window_handles

        # Switch to window and search course

        window_before = self.driver.window_handles[0]
        window_after = self.driver.window_handles[1]

        self.driver.switch_to.window(window_after)
        searchBox = self.driver.find_element(By.NAME, "course")
        searchBox.send_keys("python")
        time.sleep(2)
        self.driver.close()

        # Switch back to the parent handle
        self.driver.switch_to.window(window_before)
        self.driver.find_element(By.ID, 'name').send_keys("test success")

        # for handle in handles:
        #     if handle not in handles:
        #         self.driver.switch_to.window(handle)
        #         searchBox = self.driver.find_element(By.ID, "search-courses")
        #         searchBox.send_keys("python")
        #         time.sleep(2)
        #         self.driver.close()
        #         break

        # Switch back to the parent handle
        # self.driver.switch_to.window(parentHandle)
        # self.driver.find_element(By.ID, 'name').send_keys("test success")

    def test_switch_to_iframe(self):
        self.driver.execute_script("window.scrollBy(0,1000);")

        # you can put anything such as Id, name
        # Switch to frame using Id
        self.driver.switch_to.frame("courses-iframe")
        # Switch to frame using name
        #self.driver.switch_to.frame("iframe-name")
        # Switch to frame using numbers
        #self.driver.switch_to.frame(0)
        time.sleep(2)
        # Search course
        searchBox = self.driver.find_element(By.NAME, "course")
        searchBox.send_keys("python")
        time.sleep(2)

        # Switch back to the parent frame
        self.driver.switch_to.default_content()
        self.driver.execute_script("window.scrollBy(0,-1000);")
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()