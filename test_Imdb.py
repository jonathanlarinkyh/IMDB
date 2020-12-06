import time
import unittest
import page
from page import IMDB_menu_community, IMDBMainPage
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import HtmlTestRunner


options = webdriver.FirefoxOptions()
options.add_argument('ignore-certificate-errors')
print(help(EC.presence_of_all_elements_located))


def webdriver_Firefox():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver


def webdriver_Firefox_headless():
    options.headless = True
    driver = webdriver.Firefox()
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
        main_page.click_IMDB_Nav()


class test_imdb_menu_community(unittest.TestCase):
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

class test_imdb_menu_community(unittest.TestCase):
    def __init__(self, methodName: str = ...):
        super().__init__(methodName)

    def setUp(self):
        self.driver = webdriver_Firefox()
        self.driver.get("https://www.imdb.com")

    def est_click_menu(self):
        main_page = page.IMDBMainPage(self.driver)
        main_page.click_menu_dd()

    def test_click_contributor_zone(self):
        main_page = page.IMDB_menu_community(self.driver)
        main_page.click_contributor_zone()


class test_imdb_menu_community(unittest.TestCase):
    def __init__(self, methodName: str = ...):
        super().__init__(methodName)

    def setUp(self):
        self.driver = webdriver_Firefox()
        self.driver.get("https://www.imdb.com")

    def est_click_menu(self):
        main_page = page.IMDBMainPage(self.driver)
        main_page.click_menu_dd()

    def test_click_polls(self):
        main_page = page.IMDB_menu_community(self.driver)
        main_page.click_polls()


class test_imdb_dropdown(PageObject):
    def __init__(self, driver: webdriver.Firefox):
        self.driver = driver

    def click_help_center(self):
        self.driver.find_element_by_css_selector(".dropdown:nth-child(1) > .dropdown-button").click()

    def click_contributor(self):
        self.driver.find_element_by_css_selector(".dropdown:nth-child(2) > .dropdown-button").click()

    def click_polls(self):
        self.driver.find_element_by_css_selector(".dropdown:nth-child(3) > .dropdown-button").click()




if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_name="Nuri_Test_IMDB"))