import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class WaitingTest(unittest.TestCase):
    def setUp(self):
        baseUrl = "https://www.phptravels.net/"
        s = Service("D:\selenium\drivers\chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get(baseUrl)

    def test_select_date(self):
        # click Flights tab
        self.driver.find_element(By.LINK_TEXT, 'Flights').click()

        # click departing date
        departure_filed = self.driver.find_element(By.ID, 'departure')
        departure_filed.click()

        # find the departing date to be selected
        dateToSelect = self.driver.find_element(By.XPATH,
                                                '//*[@id="fadein"]//tr[5]/td[1]')
        dateToSelect.click()
        self.assertEqual('27-03-2022', departure_filed.get_attribute('value'))

    def test_destination(self):
        dep_input_text = "Toronto"
        dep_result_text = "Lester B Pearson Intl"
        arr_input_text = "Incheon"
        arr_result_text = "Incheon Intl"

        self.driver.find_element(By.LINK_TEXT, 'Flights').click()

        # Departure Test
        input_filed = self.driver.find_element(By.NAME, 'from')
        input_filed.send_keys(dep_input_text)
        dep_result = self.driver.find_element(By.CLASS_NAME, 'autocomplete-results')
        dep_results = dep_result.find_elements(By.TAG_NAME, 'strong')
        for result in dep_results:
            #print(result.text)
            if dep_result_text in result.text:
                result.click()
                break

        # Arrive Test
        input_filed = self.driver.find_element(By.NAME, 'to')
        input_filed.send_keys(arr_input_text)
        arr_result = self.driver.find_element(By.CLASS_NAME, 'autocomplete-results')
        arr_results = dep_result.find_elements(By.TAG_NAME, 'strong')

        for result in arr_results:
            if arr_result_text in result.text:
                result.click()
                break
        # Search Click
        self.driver.find_element(By.ID, 'flights-search').click()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()