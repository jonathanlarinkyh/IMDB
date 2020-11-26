import unittest
import HtmlTestRunner
# import test suite

if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    HtmlTestRunner.HTMLTestRunner().run(test_suite)
