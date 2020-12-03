import unittest
from Amaj_Script import test_IMBD_Nav, IMDBTest, test_Awards_and_Events_Oscars, test_imdb_menu
from Chris_script import IMDBCelebsTVShows

import HtmlTestRunner


if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(IMDBCelebsTVShows))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(IMDBTest))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_IMBD_Nav))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_imdb_menu))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_Awards_and_Events_Oscars))

    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_name="IMDB_Tests_PVT2019",
                                                           output='Reports/', template='html_Temp/Template.html')).runTests(test_suite)