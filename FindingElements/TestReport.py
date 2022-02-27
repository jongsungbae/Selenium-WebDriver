import unittest
import os
from HtmlTestRunner import HTMLTestRunner
from FindingElementsTest import FindingElementsTest

# get the directory path to output report file
dir = os.getcwd()

# get all tests from search Test and homepage Test
homepage_test = unittest.TestLoader().loadTestsFromTestCase(FindingElementsTest)

smoke_tests = unittest.TestSuite([homepage_test])


# configure HTMLTestRunner options
runner = HTMLTestRunner(
    output='smokeTest'
)

# Run the suite using HTMLTestRunner
runner.run(smoke_tests)