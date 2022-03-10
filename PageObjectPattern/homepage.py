from selenium.webdriver.common.by import By
from basePage import BasePage
from basePage import InvalidPageException

class HomePage(BasePage):
    _home_page_slideshow_locator = 'dev.slideshow-container'

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)

    def _validate_page(self, driver):
        try:
            driver.find_element(By.NAME, self._home_page_slideshow_locator)
        except:
            raise InvalidPageException("Home Page not loaded")
        
