import time
import unittest

import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')
print(help(EC.presence_of_all_elements_located))


def webdriver_chrome():
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver


def webdriver_chrome_headless():
    options.headless = True
    driver = webdriver.Chrome(chrome_options=options)
    driver.set_window_size(1920, 1080)
    driver.implicitly_wait(10)
    return driver


def webdriver_factory():
    return webdriver_chrome_headless()


class IMDBTest(unittest.TestCase):
    # declare variable to store the URL to be visited
    base_url = "https://www.imdb.com"
    time.sleep(2)

    # --- Pre - Condition ---

    def setUp(self):
        # declare and initialize driver variable
        self.driver = webdriver.Chrome()
        # close the app dialogue page
        self.driver.get("https://imdb.com")
        time.sleep(5)

    def tearDown(self):
        self.driver.close()


class test_IMBD_Nav(unittest.TestCase):
    base_url = "https://www.imdb.com"

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.target_url = "https://www.imdb.com"

    def setUp(self):
        self.driver = webdriver_chrome()
        self.driver.get("https://www.imdb.com")

    def test_page_access(self):
        main_page = self.driver.get("https://imdb.com")

        pass


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_name="IMDB_Tests",
                                                           output='C:/Users/AmAj/Desktop/Python '
                                                                  'Projects/IMDB/Jonathan/Reports'))
