import unittest
import HtmlTestRunner
from awards_amaj import IMDB_Home_Page_test, test_IMBD_Nav, test_imdb_menu, test_Awards_and_Events_Oscars

if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(IMDB_Home_Page_test))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_IMBD_Nav))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_imdb_menu))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_Awards_and_Events_Oscars))
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_name="IMDB_Tests_Amaj",
                                                           output='Reports/', template='html_Temp/Temp.html')).runTests()
