import unittest
import os
from HtmlTestRunner import HTMLTestRunner
from drag_and_drop import DragAndDrop
from mouse_hover import MouseAction
from slider import Slider


dir = os.getcwd()

# get all tests from search Test and homepage Test
drag_and_drop = unittest.TestLoader().loadTestsFromTestCase(DragAndDrop)
mouse_hover = unittest.TestLoader().loadTestsFromTestCase(MouseAction)
slider = unittest.TestLoader().loadTestsFromTestCase(Slider)


# create a test suite combining search_test and homepage test
smoke_tests = unittest.TestSuite([drag_and_drop, mouse_hover, slider])

# open the report file
#outfile = open(dir + "\SmokeTestReport.html", "w")

# configure HTMLTestRunner options
runner = HTMLTestRunner(
    output='smokeTest'
)

# Run the suite using HTMLTestRunner
runner.run(smoke_tests)