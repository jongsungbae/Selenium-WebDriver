import xlrd, unittest

from ddt import ddt, data, unpack
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def get_data(file_name):
    # create an empty list to store rows
    rows = []
    # open the excel file
    book = xlrd.open_workbook(file_name)
    # get the first sheet
    sheet = book.sheet_by_index(0)
    # iterate through the sheet and get data
    for row_idx in range(1, sheet.nrows):
        rows.append(list(sheet.row_values(row_idx, 0, sheet.ncols)))
    return rows

@ddt
class SearchDDT(unittest.TestCase):
    def setUp(self):
        baseUrl = "http://magento-demo.lexiconn.com/"
        s = Service("D:\selenium\drivers\chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get(baseUrl)

    # get the data from csv file
    @data(*get_data("D://selenium//DataDrivenTest//testdata.xlsx"))
    @unpack
    def test_search(self, search_value, expected_count):
        # get the search textbox
        search_field = self.driver.find_element(By.NAME, 'q')
        search_field.clear()

        # enter search keyword and submit
        # use search_value argument to pass data
        search_field.send_keys(search_value)
        search_field.submit()

        # get all the anchor elements which have product names
        products = self.driver.find_elements(By.XPATH, "//h2[@class='product-name']/a")

        expected_count = int(expected_count)
        if expected_count > 0:
            self.assertEqual(expected_count, len(products))
        else:
            msg = self.driver.find_element(By.CLASS_NAME, 'note-msg')
            self.assertEqual("Your search returns no results.", msg.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()