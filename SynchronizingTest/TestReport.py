import unittest
import os
from HtmlTestRunner import HTMLTestRunner
from WaitingElement import WaitingTest

# get the directory path to output report file
dir = os.getcwd()

# get all tests from search Test and homepage Test
wait_test = unittest.TestLoader().loadTestsFromTestCase(WaitingTest)

smoke_tests = unittest.TestSuite([wait_test])

# configure HTMLTestRunner options
runner = HTMLTestRunner(
    output='smokeTest'
)

# Run the suite using HTMLTestRunner
runner.run(smoke_tests)