import time
import unittest
import nuri_page
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

    targetURL1 = "https://help.imdb.com/imdb?ref_=cons_nb_hlp"
    targetURL2 = "https://contribute.imdb.com/czone?ref_=nv_cm_cz"

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)

    def setUp(self):
        self.driver = webdriver_Firefox()
        self.driver.get("https://www.imdb.com")

    def test_click_menu(self):
        main_page = nuri_page.IMDBMainPage(self.driver)
        main_page.click_menu_dd()
        assert self.driver.find_element_by_link_text("Help Center").text == "Help Center"

    def test_click_help_center(self):
        main_page = nuri_page.IMDB_menu_community(self.driver)
        main_page.click_menu_dd()
        main_page.click_Help_center()
        self.assertEqual(self.driver.current_url, test_imdb_menu_community.targetURL1)

    def test_click_contributor_zone(self):
        main_page = nuri_page.IMDB_menu_community(self.driver)
        main_page.click_menu_dd()
        main_page.click_contributor_zone()
        self.assertEqual(self.driver.current_url, test_imdb_menu_community.targetURL2)

    def test_click_polls(self):
        main_page = nuri_page.IMDB_menu_community(self.driver)
        main_page.click_menu_dd()
        main_page.click_polls()
        for i in range(10):
            main_page.page_down()
        assert self.driver.find_element_by_link_text("Clear your history").text == "Clear your history"

    def tearDown(self):
        self.driver.close()





if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_name="Nuri_Test_IMDB"))