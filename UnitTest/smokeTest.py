import unittest
from searchTestsClass import SearchTestsClass
from HomePageTest import HomePageTest

# get all tests from SearchTest and Homepage Test class
search_test = unittest.TestLoader().loadTestsFromTestCase(SearchTestsClass)
homepage_test = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

# create a test suite combining search_test and homepage test
smoke_tests = unittest.TestSuite([search_test, homepage_test])

# run the suite
unittest.TextTestRunner(verbosity=2).run(smoke_tests)
