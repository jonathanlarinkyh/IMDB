import unittest
from Amaj_Script import test_IMBD_Nav, test_Awards_and_Events_Oscars, test_imdb_menu, IMDB_User_login
from Chris_script import IMDBCelebsTVShows
from Jonathan_script import IMDBPageMenu, IMDBReleaseCalendar, IMDBDVDnBlueRayReleases
from Victor_Script import IMDBWhatToWatchTestCase, IMDBNavTestCase

import HtmlTestRunner

if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(IMDBPageMenu))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(IMDBReleaseCalendar))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(IMDBDVDnBlueRayReleases))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(IMDBCelebsTVShows))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(IMDBWhatToWatchTestCase))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(IMDBNavTestCase))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_IMBD_Nav))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_imdb_menu))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_Awards_and_Events_Oscars))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(IMDB_User_login))

    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_name="IMDB_Tests_PVT2019", output='Reports/',
                                                           template='html_Temp/Template.html')).runTests()
