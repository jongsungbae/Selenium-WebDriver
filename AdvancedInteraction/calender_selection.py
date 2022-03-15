import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class WaitingTest(unittest.TestCase):
    def setUp(self):
        baseUrl = "http://www.expedia.com"
        s = Service("D:\selenium\drivers\chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get(baseUrl)

    def test_select_date(self):
        # click Flights tab
        self.driver.find_element(By.LINK_TEXT, 'Flights').click()

        # click departing date
        self.driver.find_element(By.ID, 'd1-btn').click()

        # find the departing date to be selected
        dateToSelect = self.driver.find_element(By.XPATH,
                                                "//div[@class='uitk-date-picker-month'][position()=1]//button[@data-day= '25']")
        dateToSelect.click()
        self.assertEqual('25', dateToSelect.get_attribute('data-day'))

        # find the arriving date to be selected
        dateToSelect = self.driver.find_element(By.XPATH,
                                                "//div[@class='uitk-date-picker-month'][position()=2]//button[@data-day= '30']")
        dateToSelect.click()
        self.assertEqual('30', dateToSelect.get_attribute('data-day'))





    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()