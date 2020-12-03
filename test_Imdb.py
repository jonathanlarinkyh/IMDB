import time
import unittest
import page
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.FirefoxOptions()
options.add_argument('ignore-certificate-errors')
print(help(EC.presence_of_all_elements_located))


def webdriver_Firefox():
    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver


def webdriver_Firefox_headless():
    options.headless = True
    driver = webdriver.Firefox(Firefox_options=options)
    driver.set_window_size(1920, 1080)
    driver.implicitly_wait(10)
    return driver


def webdriver_factory():
    return webdriver_Firefox_headless()


class IMDBTest(unittest.TestCase):
    # declare variable to store the URL to be visited
    base_url = "https://www.imdb.com"
    time.sleep(2)

    # --- Pre - Condition ---

    def setUp(self):
        # declare and initialize driver variable
        self.driver = webdriver.Firefox()
        # close the app dialogue page
        self.driver.get("https://imdb.com")
        time.sleep(5)

    def tearDown(self):
        self.driver.close()


class test_IMBD_Nav(unittest.TestCase):
    base_url = "www.imdb.com"

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.target_url = "https://www.imdb.com"

    def setUp(self):
        self.driver = webdriver_Firefox()
        self.driver.get("https://www.imdb.com")

    def test_page_access(self):
        main_page = test_IMBD_Nav(self.driver)
        main_page.click_IMDB()


class test_imdb_menu_community(unittest.Testcase):
    def __init__(self, methodName: str = ...):
        super().__init__(methodName)

    def setUp(self):
        self.driver = webdriver_Firefox()
        self.driver.get("https://www.imdb.com")

    def est_click_menu(self):
        main_page = page.IMDBMainPage(self.driver)
        main_page.click_menu_dd()

    def test_click_help_center(self):
        main_page = page.IMDB_menu_community(self.driver)
        main_page.click_Help_center()



if __name__ == '__main__':

    pass