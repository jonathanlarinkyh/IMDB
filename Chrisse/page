from calendar import calendar
import selenium
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.events import EventFiringWebDriver
from selenium.webdriver.support.events import AbstractEventListener
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from time import time
from datetime import datetime
import page
import HtmlTestRunner
import getpass

WEBDRIVER = "FIREFOX"


def webdriver_chrome():
    driver = webdriver.Chrome()
    print("1")
    driver.implicitly_wait(10)
    print("2")
    driver.maximize_window()
    print("3")
    return driver


def webdriver_chrome_headless():
    options = Options()
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.headless = True
    driver = webdriver.Chrome(options=options)
    print("1")
    driver.set_window_size(1920, 1080)
    print("2")
    driver.implicitly_wait(10)
    print("3")
    return driver


def webdriver_firefox():
    driver = webdriver.Firefox(executable_path=r'C:\Users\Chrisse\Desktop\Testautomation\geckodriver.exe')
    print("1")
    driver.implicitly_wait(10)
    print("2")
    driver.maximize_window()
    print("3")
    return driver

"""def webdriver_
    webdriver.Android"""

def webdriver_factory():
    if WEBDRIVER == "CHROME":
        return webdriver_chrome()
    elif WEBDRIVER == "CHROME_HEADLESS":
        return webdriver_chrome_headless()
    elif WEBDRIVER == "FIREFOX":
        return webdriver_firefox()
    else:
        return webdriver_chrome()

def print_name(f):
    def inner(self):
        print("running ", f.__name__)
        f(self)
        print("done ", f.__name__)
    return inner


class ScreenshotListener(AbstractEventListener):
    def __init__(self, base_name):
        self.base_name = base_name
        self.tmn = ""
        self.now = ""

    def get_test_method_name(self, tmn, now):
        self.tmn = tmn
        self.now = now

    def on_exception(self, exception, driver: webdriver.Chrome):
        driver.get_screenshot_as_file(self.base_name + self.tmn + self.now + ".png")


class KYHPageObject(unittest.TestCase):
    targetURL = "https://kyh.se/utbildningar/teknisk-testare/"
    targetURL2 = "https://kyh.se/om-oss/vad-ar-yh-utbildning/"
    targetURL3 = "https://kyh.se/ledigajobb/"
    targetURL4 = "https://kyh.se/inspiration/panelsamtal2019/"
    targetURL5 = "https://apply.yh-antagning.se/Application/"

    def setUp(self):
        self.driver = webdriver_factory()
        print("4")
        self.listener = ScreenshotListener("reports/screenshots/navtest")
        print("5")
        self.driver = EventFiringWebDriver(self.driver, self.listener)
        print("6")
        self.driver.get("https://www.kyh.se")
        print("7")


    """def test_nav_through_dropdown_with_page_object(self):
        main_page = page.KYHMainPage(self.driver)
        self.listener.get_test_method_name("_nav_through_dd")
        main_page.click_vara_utbildningar_dd()
        main_page.click_it_in_dd()
        vara_utbildningar = page.VaraUtbildningar(self.driver)
        vara_utbildningar.click_goteborg()
        vara_utbildningar.click_page_down()
        vara_utbildningar.click_pvt()
        self.assertEqual(self.driver.current_url, KYHPageObject.targetURL, msg="URL doesn't match")"""

    @print_name
    def test_om_kyh_om_oss(self):
        main_page = page.OmKyh(self.driver)
        self.listener.get_test_method_name("_om_kyh", datetime.now().strftime(" %H.%M.%S, %m.%d.%Y"))
        main_page.click_om_kyh_dd()
        main_page.click_om_oss()
        main_page.click_vad_ar_yh_utbildning()
        self.assertEqual(self.driver.current_url, KYHPageObject.targetURL2, msg="URL doesn't match")

    @print_name
    def test_kontakta_oss(self):
        main_page = page.KontaktaOss(self.driver)
        self.listener.get_test_method_name("_kontakta_oss", datetime.now().strftime(" %H.%M.%S, %m.%d.%Y"))
        main_page.click_kontakta_oss_dd()
        main_page.click_kontakta_oss()
        main_page.click_jag_vill_jobba_hos_er()
        main_page.click_lediga_jobb()
        self.assertEqual(self.driver.current_url, KYHPageObject.targetURL3)

    @print_name
    def test_inspiration(self):
        main_page = page.Inspriation(self.driver)
        self.listener.get_test_method_name("_inspiration", datetime.now().strftime(" %H.%M.%S, %m.%d.%Y"))
        main_page.click_inspiration_dd()
        main_page.click_meny()
        main_page.click_event()
        main_page.click_senaste()
        self.assertEqual(self.driver.current_url, KYHPageObject.targetURL4)

    @print_name
    def test_antagning(self):
        main_page = page.Antagning(self.driver)
        self.listener.get_test_method_name("_antagning", datetime.now().strftime(" %H.%M.%S, %m.%d.%Y"))
        main_page.click_antagning_dd()
        main_page.click_antagning()
        main_page.click_page_down()
        main_page.click_page_down()
        main_page.click_page_down()
        main_page.click_till_ansokan()
        self.assertTrue(self.driver.current_url, KYHPageObject.targetURL5)


    """def test_foo(self):
        main_page = page.KYHMainPage(self.driver)
        main_page.click_vara_utbildningar_dd()
        main_page.click_it_in_dd()

        vara_utbildningar = page.VaraUtbildningar(self.driver)
        vara_utbildningar.click_distans()
        time.sleep(4)
        vara_utbildningar.click_goteborg()
        time.sleep(4)

    def test_nav_through_dropdown_samh(self):
        main_page = page.KYHMainPage(self.driver)

        main_page.click_vara_utbildningar_dd()
        main_page.click_samhallsbyggnad_in_dd()"""




    def tearDown(self):
        print("Tearing down test")
        self.driver.close()


if __name__ == '__main__':
    WEBDRIVER = "CHROME"
    #unittest.main(verbosity=2)
    #template_args = {
    #    "screenshots": ""
    #}

    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(template="templates/templates.html",
                                                           report_title="Testrapport Chrisse"), verbosity=2)