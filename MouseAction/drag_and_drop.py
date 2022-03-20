import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class DragAndDrop(unittest.TestCase):
    def setUp(self):
        baseUrl = "https://jqueryui.com/droppable/"
        s = Service("E:\selenium\drivers\chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get(baseUrl)

    def test_mouse_hover(self):
        self.driver.switch_to.frame(0)
        fromElement = self.driver.find_element(By.ID, 'draggable')
        toElement = self.driver.find_element(By.ID, 'droppable')
        time.sleep(2)
        try:
            actions = ActionChains(self.driver)
            actions.drag_and_drop(fromElement, toElement).perform()
            #actions.click_and_hold(fromElement).move_to_element(toElement).release().perform()
            print("Drag and drop element successful")
            time.sleep(2)
        except:
            print("Fail")



    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()