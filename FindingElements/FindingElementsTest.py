import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class FindingElementsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # create chrome session
        baseUrl = "http://automationpractice.com/index.php"
        s = Service("E:\selenium\drivers\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=s)
        # cls.driver = webdriver.Chrome("E:\selenium\drivers\chromedriver.exe")
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get(baseUrl)

    def test_search_text_field_value(self):
        # get the search box using Xpath
        search_field = self.driver.find_element(By.ID, 'search_query_top')
        # Check the value
        self.assertEqual("Search", search_field.get_attribute("placeholder"))

    def test_search_button_enabled(self):
        # get the search button
        searchBtn = self.driver.find_element(By.NAME, 'submit_search')
        # check Search button is enabled
        self.assertTrue(searchBtn.is_enabled())

    def test_women_link_is_displayed(self):
        # get the Women link
        women_link = self.driver.find_element(By.LINK_TEXT, 'WOMEN')
        # check link text is displayed/visible
        self.assertTrue(women_link.is_displayed())

    def test_women_partial_link(self):
        # get the all the links with women text
        women_links = self.driver.find_elements(By.PARTIAL_LINK_TEXT, 'women')
        # check women partial links
        self.assertTrue(2, len(women_links))

    def test_count_of_contents(self):
        # get content list
        content_list = self.driver.find_element(By.CLASS_NAME, 'tab-content')
        # get image from the content lists
        contents = content_list.find_element(By.TAG_NAME, 'li')
        # check
        self.assertEqual(7, len(contents))

    def test_promotion(self):
        # get promotion
        promo = self.driver.find_element(By.XPATH, '//*[@id="htmlcontent_top"]/ul/li[1]/a/img')
        # check display promo
        self.assertTrue(promo.is_displayed())
        # click promo
        promo.click()
        # back to previous page
        self.driver.back()

    def test_shopping_cart__status(self):
        empty_status = self.driver.find_element(By.XPATH, '//*[@id="header"]/div[3]/div/div/div[3]/div/a/span[5]')
        if (self.assertTrue(empty_status)):
          empty_status.click()
        empty_text = self.driver.find_element(By.CLASS_NAME, 'alert-warning').text
        self.assertEqual("Your shopping cart is empty.", empty_text)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
