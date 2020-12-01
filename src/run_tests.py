import unittest
import HtmlTestRunner
from IMDB.src import IMDB_Menu_Movies


if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(IMDB_Menu_Movies.IMDBPageMenu))

    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(IMDB_Menu_Movies.IMDBReleaseCalendar))

    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(IMDB_Menu_Movies.IMDBDVDnBlueRayReleases))

    HtmlTestRunner.HTMLTestRunner().run(test_suite)
