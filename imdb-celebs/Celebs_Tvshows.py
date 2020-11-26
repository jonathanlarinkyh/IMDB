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

    targetURL0 = "https://www.imdb.com/?ref_=nv_home"
    targetURL1 = "https://www.imdb.com/search/name/?birth_monthday=" + datetime.now().strftime("%m-%d") \
                 + "&ref_=nv_cel_brn"
    targetURL2 = "https://www.imdb.com/search/name/?gender=male,female&sort=birth_date,asc&ref_=rlm"
    targetURL3 = "https://www.imdb.com/list/ls094369917/?ref_=ls_mv_sm"
    targetURL4 = "https://help.imdb.com/article/imdb/track-movies-tv/ratings-faq/G67Y87TFYYP6TWAV#"
    targetURL5 = "https://www.imdb.com/search/title/?title_type=tv_series,tv_miniseries&genres=documentary&sort=runtime,asc&start=51&view=simple"
    targetURL6 = "https://www.imdb.com/ap/cvf/request?arb="
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
        #time.sleep(5)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Born Today")))
        element.click()
        #main_page.click_born_today()
        self.assertEqual(self.driver.current_url, IMDBCelebsTVShows.targetURL1)

    @print_name
    def test_celebs_most_popular(self):
        main_page = page.CelebsMostPopular(self.driver)
        menu = page.Menu(self.driver)
        self.listener.get_test_method_name("_celebs_most_popular", datetime.now().strftime(" %H.%M.%S, %m.%d.%Y"))
        menu.click_menu()
        main_page.click_most_popular()
        main_page.click_birth_date()
        #time.sleep(5)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[2]/a[3]")))

        for i in range(15):
            main_page.click_page_down()
        self.assertEqual(self.driver.current_url, IMDBCelebsTVShows.targetURL2)

    @print_name
    def test_celebs_celebrity_news(self):
        main_page = page.CelebsCelebrityNews(self.driver)
        menu = page.Menu(self.driver)
        self.listener.get_test_method_name("_celebs_celebrity_news", datetime.now().strftime(" %H.%M.%S, %m.%d.%Y"))
        menu.click_menu()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Celebrity News")))
        element.click()
        #main_page.click_celebrity_news()
        #time.sleep(2)
        for i in range(15):
            main_page.click_page_down()
        main_page.click_load_more()
       # time.sleep(3)
        for i in range(15):
            main_page.click_page_down()
        #time.sleep(5)
        assert self.driver.find_element_by_xpath("//h3[contains(.,'Recently Viewed')]").text == "Recently Viewed"


    @print_name
    def test_tvshows_whats_on_tv(self):
        main_page = page.TvshowsWhatsOnTV(self.driver)
        menu = page.Menu(self.driver)
        self.listener.get_test_method_name("_tvshows_whats_on_tv", datetime.now().strftime(" %H.%M.%S, %m.%d.%Y"))
        menu.click_menu()
        main_page.click_whats_on_tv()
        #time.sleep(2)
        for i in range(15):
            main_page.click_page_down()
        main_page.click_see_full_gallery()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, ".article:nth-child(27) .position_bottom")))
        main_page.click_grid()
       # time.sleep(3)
        self.assertEqual(self.driver.current_url, IMDBCelebsTVShows.targetURL3)

    @print_name
    def test_tcshows_top_rated(self):

        main_page = page.TvshowsTopRated(self.driver)
        menu = page.Menu(self.driver)
        self.listener.get_test_method_name("_tvshows_top_rated", datetime.now().strftime(" %H.%M.%S, %m.%d.%Y"))
        menu.click_menu()
        main_page.click_top_rated()
        main_page.click_sort_by()
        main_page.click_number_of_ratings()
        main_page.click_enter()
        for i in range(21):
            main_page.click_page_down()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Learn more about how list ranking is determined.")))
        element.click()
        self.assertEqual(self.driver.current_url, IMDBCelebsTVShows.targetURL4)


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
        self.assertEqual(self.driver.current_url, IMDBCelebsTVShows.targetURL5)

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

        assert self.driver.find_element_by_link_text("laser-ball")

    @print_name
    def test_tvshows_tvnews(self):
        main_page = page.TvshowsTvnews(self.driver)
        menu = page.Menu(self.driver)
        self.listener.get_test_method_name("_tvshows_tvnews", datetime.now().strftime(" %H.%M.%S, %m.%d.%Y"))
        menu.click_menu()
        main_page.click_tvnews()
        main_page.click_second_article()
        assert self.driver.find_element_by_xpath("//section[@id='news-article-list']/article[2]/header/h2/a")


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
        for i in range(3):
            self.driver.back()
        #assert self.driver.find_element_by_link_text("data;")
        self.assertEqual(self.driver.current_url, IMDBCelebsTVShows.targetURL0)

    @print_name
    def test_create_user(self):
        main_page = page.CreateUser(self.driver)
        self.listener.get_test_method_name("_create_user", datetime.now().strftime(" %H.%M.%S, %m.%d.%Y"))
        main_page.click_sign_in()
        main_page.click_create_account()
        main_page.generate_name_email()
        main_page.generate_password()
        main_page.create()
        time.sleep(5)
        if self.driver.find_element_by_xpath("//*[@id='cvf-page-content']/div/div"):
            main_page.click_hear_letters()
            time.sleep(5)
            el = self.driver.find_element_by_xpath("//*[@id='cvf-page-content']/div/div/div/div[2]/div/audio")
            action = webdriver.common.ActionChains(self.driver)
            action.move_to_element_with_offset(el, 0, 5)
            action.click()
            action.perform()


            time.sleep(5)


        else:
            assert self.driver.find_element_by_xpath("//a[contains(text(),'Sign-In')]")
            time.sleep(4)


    def tearDown(self):
        print("Tearing down test")
        self.driver.close()


if __name__ == '__main__':
    WEBDRIVER = "CHROME"

    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(template="templates/templates.html",
                                                           report_title="Testrapport Chrisse"), verbosity=2)