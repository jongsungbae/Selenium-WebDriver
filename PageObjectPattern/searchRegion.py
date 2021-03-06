from selenium.webdriver.common.by import By

from basePage import BasePage
from basePage import InvalidPageException
from productPage import ProductPage

class SearchRegion(BasePage):
    _search_box_locator = 'q'

    def __init__(self, driver):
        super(SearchRegion, self).__init__(driver)

    def searchFor(self, term):
        search_field = self.driver.find_element(By.NAME, self._search_box_locator)
        search_field.clear()
        search_field.send_keys(term)
        search_field.submit()
        return SearchResults(self.driver)

class SearchResults(BasePage):
    _product_list_locater = 'ul.products-grid > li'
    _product_name_locator = 'h2.product-name > a'
    _product_image_link = 'a.product-image'
    _product_title_locator = 'div.page-title'
    _product_count = 0
    _products = {}

    def __init__(self, driver):
        super(SearchResults, self).__init__(driver)
        results = self.driver.find_elements(By.CSS_SELECTOR, self._procut_list_locator)
        for product in results:
            name = product.find_element(By.CSS_SELECTOR, self._product_name_locator).text
            self._products[name] = product.find_element(By.CSS_SELECTOR, self._product_image_link)

    def _validate_page(self, driver):
        if 'Search results for' not in driver.title:
            raise InvalidPageException('Search results not loaded')

    @property
    def product_count(self):
        return len(self._products)

    def get_products(self):
        return self._products

    def open_product_page(self, product_name):
        self._products[product_name].click()
        return ProductPage(self.driver)







