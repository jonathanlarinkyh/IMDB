from calendar import calendar
import selenium
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.events import EventFiringWebDriver
from selenium.webdriver.support.events import AbstractEventListener
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
import time
from datetime import datetime
import page
import HtmlTestRunner
from selenium.webdriver.support.ui import Select
import getpass


WEBDRIVER = "CHROME"


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


class IMDBCelebsTVShows(unittest.TestCase):

    targetURL1 = "https://www.imdb.com/search/name/?birth_monthday=11-19&ref_=nv_cel_brn"
    targetURL2 = "tps://www.imdb.com/search/name/?gender=male%2Cfemale&ref_=nv_cel_m"
    def setUp(self):
        self.driver = webdriver_factory()
        print("4")
        self.listener = ScreenshotListener("reports/screenshots/navtest")
        print("5")
        self.driver = EventFiringWebDriver(self.driver, self.listener)
        print("6")
        self.driver.get("https://www.imdb.com/?ref_=nv_home")
        print("7")


    @print_name
    def test_celebs_born_today(self):
        main_page = page.CelebsBornToday(self.driver)
        menu = page.Menu(self.driver)
        self.listener.get_test_method_name("_celebs_born_today", datetime.now().strftime(" %H.%M.%S, %m.%d.%Y"))
        menu.click_menu()
        time.sleep(5)
        main_page.click_born_today()
        self.assertEqual(self.driver.current_url, IMDBCelebsTVShows.targetURL1)

    @print_name
    def test_celebs_most_popular(self):
        main_page = page.CelebsMostPopular(self.driver)
        menu = page.Menu(self.driver)
        self.listener.get_test_method_name("_celebs_most_popular", datetime.now().strftime(" %H.%M.%S, %m.%d.%Y"))
        menu.click_menu()
        main_page.click_most_popular()
        main_page.click_birth_date()
        time.sleep(5)
        for i in range(15):
            main_page.click_page_down()

        self.assertEqual(self.driver.current_url, IMDBCelebsTVShows.targetURL2)

    @print_name
    def test_celebs_celebrity_news(self):
        main_page = page.CelebsCelebrityNews(self.driver)
        menu = page.Menu(self.driver)
        self.listener.get_test_method_name("_celebs_celebrity_news", datetime.now().strftime(" %H.%M.%S, %m.%d.%Y"))
        menu.click_menu()
        time.sleep(2)
        main_page.click_celebrity_news()
        time.sleep(2)
        self.assertEqual()

        for i in range(15):
            main_page.click_page_down()
        main_page.click_load_more()
        time.sleep(5)

    @print_name
    def test_tvshows_whats_on_tv(self):
        main_page = page.TvshowsWhatsOnTV(self.driver)
        menu = page.Menu(self.driver)
        self.listener.get_test_method_name("_tvshows_whats_on_tv", datetime.now().strftime(" %H.%M.%S, %m.%d.%Y"))
        menu.click_menu()
        main_page.click_whats_on_tv()
        time.sleep(2)
        for i in range(15):
            main_page.click_page_down()
        main_page.click_see_full_gallery()
        time.sleep(4)
        main_page.click_grid()
        time.sleep(3)

    @print_name
    def test_tcshows_top_rated(self):

        main_page = page.TvshowsTopRated(self.driver)
        menu = page.Menu(self.driver)
        self.listener.get_test_method_name("_tvshows_top_rated", datetime.now().strftime(" %H.%M.%S, %m.%d.%Y"))
        menu.click_menu()
        main_page.click_top_rated()
        main_page.click_sort_by()
        time.sleep(3)
        main_page.click_number_of_ratings()
        time.sleep(4)
        main_page.click_enter()
        for i in range(21):
            main_page.click_page_down()
        time.sleep(3)
        main_page.click_learn_more()
        time.sleep(3)

    @print_name
    def test_tcshows_most_popular(self):
        main_page = page.TvshowsMostPopular(self.driver)
        menu = page.Menu(self.driver)
        self.listener.get_test_method_name("_tvshows_most_popular", datetime.now().strftime(" %H.%M.%S, %m.%d.%Y"))
        menu.click_menu()
        main_page.click_most_popular()
        main_page.click_doc()
        main_page.click_runtime()
        main_page.click_next()
        main_page.click_compact()

    @print_name
    def test_tcshows_browse_tvshow(self):
        main_page = page.TvshowsBrowseTvshows(self.driver)
        menu = page.Menu(self.driver)
        self.listener.get_test_method_name("_tvshows_browse_tvshow", datetime.now().strftime(" %H.%M.%S, %m.%d.%Y"))
        menu.click_menu()
        main_page.click_browse()
        main_page.click_search()
        main_page.click_searchfield()
        main_page.click_go()
        time.sleep(4)

    @print_name
    def test_tvshows_tvnews(self):
        main_page = page.TvshowsTvnews(self.driver)
        menu = page.Menu(self.driver)
        self.listener.get_test_method_name("_tvshows_tvnews", datetime.now().strftime(" %H.%M.%S, %m.%d.%Y"))
        menu.click_menu()
        main_page.click_tvnews()
        main_page.click_second_article()
        time.sleep(4)

    @print_name
    def test_tvshows_indian(self):
        main_page = page.TvshowsIndian(self.driver)
        menu = page.Menu(self.driver)
        self.listener.get_test_method_name("_tvshows_indian", datetime.now().strftime(" %H.%M.%S, %m.%d.%Y"))
        menu.click_menu()
        main_page.click_indian_tv()
        main_page.click_top_rated()
        main_page.click_see_more()
        main_page.click_descending()
        for i in range(4):
            self.driver.back()


    def tearDown(self):
        print("Tearing down test")
        self.driver.close()


if __name__ == '__main__':
    WEBDRIVER = "CHROME"

    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(template="templates/templates.html",
                                                           report_title="Testrapport Chrisse"), verbosity=2)