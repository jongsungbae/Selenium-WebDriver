import unittest
import os
from HtmlTestRunner import HTMLTestRunner
from switch_to_window import SwitchTest


# get the directory path to output report file
dir = os.getcwd()

# get all tests from search Test and homepage Test
switch_test = unittest.TestLoader().loadTestsFromTestCase(SwitchTest)


# create a test suite combining search_test and homepage test
smoke_tests = unittest.TestSuite([switch_test])

# open the report file
#outfile = open(dir + "\SmokeTestReport.html", "w")

# configure HTMLTestRunner options
runner = HTMLTestRunner(
    output='smokeTest'
)

# Run the suite using HTMLTestRunner
runner.run(smoke_tests)