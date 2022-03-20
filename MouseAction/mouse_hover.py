import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class MouseAction(unittest.TestCase):
    def setUp(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        s = Service("E:\selenium\drivers\chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get(baseUrl)

    def test_mouse_hover(self):
        self.driver.execute_script("window.scrollBy(0, 600);")
        time.sleep(2)

        hoverElement = self.driver.find_element(By.ID, 'mousehover')

        itemToClickLocator = ".//div[@class='mouse-hover-content']//a[text()='Reload']"

        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(hoverElement).perform()
            print("Mouse Hovered on element")
            time.sleep(2)
            topLink = self.driver.find_element(By.XPATH, itemToClickLocator)
            actions.move_to_element(topLink).click().perform()
            print("Item Clicked")
        except:
            print("Mouse Hover failed on element")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()