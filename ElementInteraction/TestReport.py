import unittest
import os
from HtmlTestRunner import HTMLTestRunner
# from RegisterNewUser import RegisterNewUser
# from LoginUser import LoginUser
from NavigationTest import NavigationTest
from AlertTest import AlertTest

# get the firectory path to output report file
dir = os.getcwd()

# get all tests from test
# registerNewUser = unittest.TestLoader().loadTestsFromTestCase(RegisterNewUser)
# loginUser = unittest.TestLoader().loadTestsFromTestCase(LoginUser)
naviTest = unittest.TestLoader().loadTestsFromTestCase(NavigationTest)
alertTest = unittest.TestLoader().loadTestsFromTestCase(AlertTest)
smoke_tests = unittest.TestSuite([naviTest, alertTest])

# configure HTMLTestRunner options
runner = HTMLTestRunner(
    output='smokeTest'
)

# Run the suite using HTMLTestRunner
runner.run(smoke_tests)