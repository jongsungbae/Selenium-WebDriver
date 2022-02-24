import unittest
import os
from HtmlTestRunner import HTMLTestRunner
from searchTestsClass import SearchTestsClass
from HomePageTest import HomePageTest

# get the directory path to output report file
dir = os.getcwd()

# get all tests from search Test and homepage Test
search_test = unittest.TestLoader().loadTestsFromTestCase(SearchTestsClass)
homepage_test = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

# create a test suite combining search_test and homepage test
smoke_tests = unittest.TestSuite([search_test, homepage_test])

# open the report file
#outfile = open(dir + "\SmokeTestReport.html", "w")

# configure HTMLTestRunner options
runner = HTMLTestRunner(
    output='smokeTest'
)

# Run the suite using HTMLTestRunner
runner.run(smoke_tests)