import unittest
import htmltestrunner
import imdb_nagivation_tests


class HtmlTestRunner(object):


if __name__ == '__main__':
    pass
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(kyh_navigation_tests.KYHTestCaseNavPVT))
    HtmlTestRunner.HTMLTestRunner(template="report_templates/report_template.html").run(test_suite)� < img
    src = {{test_case.stdout}} >