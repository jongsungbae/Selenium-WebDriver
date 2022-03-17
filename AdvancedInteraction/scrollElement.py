import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class ScrollElement(unittest.TestCase):
    def setUp(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        s = Service("D:\selenium\drivers\chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get(baseUrl)

    def test_scroll(self):
        # check size of windows using javascript
        height = self.driver.execute_script("return window.innerHeight;")
        width = self.driver.execute_script("return window.innerWidth;")
        print("Height: " + str(height))
        print("Width: " + str(width))

        # Scroll Down
        self.driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(2)

        # Scroll Up
        self.driver.execute_script("window.scrollBy(0, -1000);")
        time.sleep(2)

        # Scroll Element Into View
        element = self.driver.find_element(By.ID, "mousehover")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0, -100);")

        # Native way to scroll element into view
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0, -600);")
        location = element.location_once_scrolled_into_view
        print("location: " + str(location))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
