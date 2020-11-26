from datetime import datetime
import time

from selenium.webdriver.support.abstract_event_listener import AbstractEventListener
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

import aa_page
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
        # Screenshot Path
        self.listener = ScreenshotListener("SC_Amaj/")
        self.driver = EventFiringWebDriver(self.driver, self.listener)
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
        # Screenshot Path

    def test_page_access(self):
        main_page = self.driver.get("https://imdb.com")

    def tearDown(self):
        self.driver.close()


class test_imdb_menu(unittest.TestCase):

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)

    def setUp(self):
        self.driver = webdriver_chrome()
        self.driver.get("https://www.imdb.com")

    #        page.IMDBMainPage(self.driver).accept_cookies()

    def test_click_menu(self):
        main_page = aa_page.IMDBMainPage(self.driver)
        main_page.click_menu_dd()
        # self.listener.get_test_method_name("_click_menu", datetime.now().strftime("%H.%M.%S, %m.%d.%Y"))

    def test_001_menu_oscars(self):
        main_page = aa_page.IMDB_menu_awards(self.driver)
        main_page.click_menu_dd()
        main_page.click_oscars()

        time.sleep(5)

    def test_002_menu_BPW(self):
        main_page = aa_page.IMDB_menu_awards(self.driver)
        main_page.click_menu_dd()
        time.sleep(2)
        main_page.click_best_picture_Winner()
        time.sleep(5)

    def test_003_menu_Golden_Globes(self):
        main_page = aa_page.IMDB_menu_awards(self.driver)
        main_page.click_menu_dd()
        time.sleep(2)
        main_page.click_Golden_Globes()

        time.sleep(5)

    def foo_test_004_menu_Emmys(self):
        main_page = aa_page.IMDB_menu_awards(self.driver)
        main_page.click_menu_dd()
        time.sleep(2)
        main_page.click_Emmys()
        self.assertEqual(self.driver.find_element_by_xpath("//h1[normalize-space()='EMMYS']").text,
                         "EMMYS", msg="Not Emmys")
        self.driver.save_screenshot("C:/Users/AmAj/Desktop/Python Projects/IMDB/Jonathan/SC_Amaj/Emmys.png")
        time.sleep(5)

    def foo_test_005_menu_STARmeter_Awards(self):
        main_page = aa_page.IMDB_menu_awards(self.driver)
        main_page.click_menu_dd()
        time.sleep(2)
        main_page.click_STARmeter_Awards()
        self.assertEqual(self.driver.find_element_by_xpath("//h1[normalize-space()='IMDb STARmeter AWARDS']").text,
                         "IMDb STARmeter AWARDS", msg="Wrong Page Not STARmeter Awards")
        self.driver.save_screenshot("C:/Users/AmAj/Desktop/Python Projects/IMDB/Jonathan/SC_Amaj/Starmeter Award.png")
        time.sleep(5)

    def foo_test_006_menu_SD_Comic_Con(self):
        main_page = aa_page.IMDB_menu_awards(self.driver)
        main_page.click_menu_dd()
        time.sleep(2)
        main_page.click_SanDiego_Comic_Con()
        self.assertEqual(self.driver.find_element_by_xpath("//*[@id='widget-nav']/div[1]/div/a/h1").text,
                         "SAN DIEGO COMIC-CON", msg="Wrong Page Not SD COMIC CON")
        self.driver.save_screenshot("C:/Users/AmAj/Desktop/Python Projects/IMDB/Jonathan/SC_Amaj/SD Comic Con.png")
        time.sleep(5)

    def foo_test_007_menu_NY_Comic_Con(self):
        main_page = aa_page.IMDB_menu_awards(self.driver)
        main_page.click_menu_dd()
        time.sleep(2)
        main_page.click_NY_Comic_Con()
        self.assertEqual(self.driver.find_element_by_xpath("//h1[normalize-space()='NEW YORK COMIC CON']").text,
                         "NEW YORK COMIC CON", msg="Wrong Page Not NY COMIC CON")
        self.driver.save_screenshot("C:/Users/AmAj/Desktop/Python Projects/IMDB/Jonathan/SC_Amaj/NY Comic Con.png")
        time.sleep(5)

    def foo_test_008_menu_Sundance_FF(self):
        main_page = aa_page.IMDB_menu_awards(self.driver)
        main_page.click_menu_dd()
        time.sleep(2)
        main_page.click_Sundance_Film_Festival()
        self.assertEqual(self.driver.find_element_by_xpath("//h1[normalize-space()='SUNDANCE FILM FESTIVAL']").text,
                         "SUNDANCE FILM FESTIVAL", msg="Wrong Page Not SUNDANCE FILM FESTIVAL")
        self.driver.save_screenshot("C:/Users/AmAj/Desktop/Python Projects/IMDB/Jonathan/SC_Amaj/Sundance FF.png")
        time.sleep(5)

    def foo_test_009_menu_Toronto_Intl_FF(self):
        main_page = aa_page.IMDB_menu_awards(self.driver)
        main_page.click_menu_dd()
        time.sleep(2)
        main_page.click_Toronto_Intl_Film_Festival()
        self.assertEqual(self.driver.find_element_by_xpath("//h1[normalize-space()='TORONTO INTERNATIONAL FILM FESTIVAL']").text,
                         "TORONTO INTERNATIONAL FILM FESTIVAL", msg="Wrong Page Not TORONTO INTL FILM FESTIVAL")
        self.driver.save_screenshot("C:/Users/AmAj/Desktop/Python Projects/IMDB/Jonathan/SC_Amaj/Toronto Intl FF.png")
        time.sleep(5)

    def foo_test_009_menu_AWARD_CENTRAL(self):
        main_page = aa_page.IMDB_menu_awards(self.driver)
        main_page.click_menu_dd()
        time.sleep(2)
        main_page.click_Awards_central()
        self.assertEqual(
            self.driver.find_element_by_xpath("//h1[normalize-space()='AWARDS CENTRAL']").text,
            "AWARDS CENTRAL", msg="Wrong Page Not AWARD CENTRAL")
        self.driver.save_screenshot("C:/Users/AmAj/Desktop/Python Projects/IMDB/Jonathan/SC_Amaj/Award Central.png")
        time.sleep(5)

    def foo_test_010_menu_Festival_Central(self):
        main_page = aa_page.IMDB_menu_awards(self.driver)
        main_page.click_menu_dd()
        time.sleep(2)
        main_page.click_Festival_Central()
        self.assertEqual(
            self.driver.find_element_by_xpath("//h1[normalize-space()='FESTIVAL CENTRAL']").text,
            "FESTIVAL CENTRAL", msg="Wrong Page Not FESTIVAL CENTRAL")
        self.driver.save_screenshot("C:/Users/AmAj/Desktop/Python Projects/IMDB/Jonathan/SC_Amaj/Festival Central.png")
        time.sleep(5)

    def foo_test_011_menu_All_Events(self):
        main_page = aa_page.IMDB_menu_awards(self.driver)
        main_page.click_menu_dd()
        time.sleep(2)
        main_page.click_All_Events()
        self.assertEqual(
            self.driver.find_element_by_xpath("//h1[normalize-space()='All Events']").text,
            "All Events", msg="Wrong Page Not All Events")
        self.driver.save_screenshot("C:/Users/AmAj/Desktop/Python Projects/IMDB/Jonathan/SC_Amaj/All Events.png")
        time.sleep(5)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_name="IMDB_Tests",
                                                           output='C:/Users/AmAj/Desktop/Python '
                                                                  'Projects/IMDB/Jonathan/Reports'))
