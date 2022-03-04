import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class NavigationTest(unittest.TestCase):
    def setUp(self):
        baseUrl = "http://www.google.com"
        s = Service("E:\selenium\drivers\chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get(baseUrl)

    def test_browser_navigation(self):
        driver = self.driver

        # TC1. get the search field
        search_field = self.driver.find_element(By.NAME, 'q')
        search_field.send_keys("selenium webdriver")
        search_field.submit()

        searched_link_text = self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[2]/ul/li[3]/div/div/div/div[1]/div/a/h3')
        searched_link_text.click()
        self.assertEqual("Index", driver.title)

        # TC2. driver back
        driver.back()
        self.assertTrue(WebDriverWait(self.driver, 10).until(expected_conditions.title_is('selenium webdriver - Google 검색')))

        # TC3. driver forward
        driver.forward()
        self.assertTrue(WebDriverWait(self.driver, 10).until(expected_conditions.title_is('Index')))

        # TC4. driver refresh
        driver.refresh()
        self.assertTrue(WebDriverWait(self.driver, 10).until(expected_conditions.title_is('Index')))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()





