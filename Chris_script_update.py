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
import imdb_page
import HtmlTestRunner
from selenium.webdriver.support.ui import Select
import getpass
from selenium.webdriver.common.action_chains import ActionChains


WEBDRIVER = "CHROME"


def webdriver_chrome():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver


def webdriver_chrome_headless():
    options = Options()
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 1080)
    driver.implicitly_wait(10)
    return driver


def webdriver_firefox():
    driver = webdriver.Firefox(executable_path=r'C:\Users\Chrisse\Desktop\Testautomation\geckodriver.exe')
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver


def webdriver_factory():
    if WEBDRIVER == "CHROME":
        return webdriver_chrome()
    elif WEBDRIVER == "CHROME_HEADLESS":
        return webdriver_chrome_headless()
    elif WEBDRIVER == "FIREFOX":
        return webdriver_firefox()
    else:
        return webdriver_chrome()


class IMDBCelebs(unittest.TestCase):

    targetURL0 = "https://www.imdb.com/?ref_=nv_home"
    targetURL1 = "https://www.imdb.com/search/name/?birth_monthday=" + datetime.now().strftime("%m-%d") \
                 + "&ref_=nv_cel_brn"
    targetURL2 = "https://www.imdb.com/search/name/?birth_monthday=" + datetime.now().strftime("%m-%d") + \
                     "&sort=death_date,asc&ref_=rlm"
    targetURL3 = "https://www.imdb.com/search/name/?gender=male,female&sort=birth_date,asc&ref_=rlm"

    def setUp(self):
        self.driver = webdriver_factory()
        self.driver.get("https://www.imdb.com/?ref_=nv_home")

    def test_celebs_born_today(self):
        main_page = imdb_page.CelebsBornToday(self.driver)
        menu = imdb_page.Menu(self.driver)
        menu.click_menu_dd()
        #wait = WebDriverWait(self.driver, 10)
        #element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Born Today")))
        #element.click()
        main_page.click_born_today()
        self.assertEqual(self.driver.current_url, IMDBCelebs.targetURL1)

    def test_celebs_born_today_death(self):
        main_page = imdb_page.CelebsBornToday(self.driver)
        menu = imdb_page.Menu(self.driver)
        menu.click_menu_dd()
        main_page.click_born_today()
        main_page.click_death_date()
        self.assertEqual(self.driver.current_url, IMDBCelebs.targetURL2)

    def test_celebs_most_popular(self):
        main_page = imdb_page.CelebsMostPopular(self.driver)
        menu = imdb_page.Menu(self.driver)
        menu.click_menu_dd()
        main_page.click_most_popular()
        main_page.click_birth_date()
        for i in range(15):
            main_page.page_down()
        self.assertEqual(self.driver.current_url, IMDBCelebs.targetURL3)

    def test_celebs_most_popular_death(self):
        main_page = imdb_page.CelebsMostPopular(self.driver)
        menu = imdb_page.Menu(self.driver)
        menu.click_menu_dd()
        main_page.click_most_popular()
        main_page.click_death_date()
        assert self.driver.find_element_by_xpath("//a[contains(.,'Death Date')]").text == "Death Date"

    def test_celebs_celebrity_news(self):
        main_page = imdb_page.CelebsCelebrityNews(self.driver)
        menu = imdb_page.Menu(self.driver)
        menu.click_menu_dd()
        main_page.click_celebrity_news()
        for i in range(15):
            main_page.page_down()
        main_page.click_load_more()
        for i in range(15):
            main_page.page_down()
        assert self.driver.find_element_by_xpath("//h3[contains(.,'Recently Viewed')]").text == "Recently Viewed"

    def test_celebs_celebrity_indie_news(self):
        main_page = imdb_page.CelebsCelebrityNews(self.driver)
        menu = imdb_page.Menu(self.driver)
        menu.click_menu_dd()

        main_page.click_celebrity_news()
        for l in range(2):
            main_page.page_down()
        main_page.click_indie_news()
        for l in range(3):
            for i in range(15):
                main_page.page_down()
            main_page.click_load_more()
        assert self.driver.find_element_by_xpath("//h3[contains(.,'Recently Viewed')]").text == "Recently Viewed"

    def tearDown(self):
        self.driver.close()


class IMDBTVshows(unittest.TestCase):

    targetURL4 = "https://www.imdb.com/imdbpicks/prime-video-originals/ls094369917/mediaviewer/rm1272830721/undefined?ref_=ls_mv_sm"
    targetURL5 = "https://help.imdb.com/article/imdb/track-movies-tv/ratings-faq/G67Y87TFYYP6TWAV#"
    targetURL6 = "https://www.imdb.com/search/title/?title_type=tv_series,tv_miniseries&genres=documentary&sort=runtime,asc&start=51&view=simple"
    targetURL7 = "https://www.imdb.com/news/top?ref_=nwc_sb_nwc_sm"

    def setUp(self):
        self.driver = webdriver_factory()
        self.driver.get("https://www.imdb.com/?ref_=nv_home")

    def test_tvshows_whats_on_tv(self):
        main_page = imdb_page.TvshowsWhatsOnTV(self.driver)
        menu = imdb_page.Menu(self.driver)
        menu.click_menu_dd()
        main_page.click_whats_on_tv()
        for i in range(15):
            main_page.page_down()
        main_page.click_see_full_gallery()
        main_page.click_grid()
        self.assertEqual(self.driver.current_url, IMDBTVshows.targetURL4)

    def test_tvshows_whats_on_tv_holidays(self):
        main_page = imdb_page.TvshowsWhatsOnTV(self.driver)
        menu = imdb_page.Menu(self.driver)
        menu.click_menu_dd()
        main_page.click_whats_on_tv()
        main_page.page_down()
        main_page.click_holiday()
        self.assertTrue(self.driver.current_url, "https://www.imdb.com/whats-on-tv/holiday-tv-shows-movies/rg738826752/mediaviewer/rm3377125633/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3c9deb43-b3f2-4d0c-8761-b0a25308fa9d&pf_rd_r=QDCMRQYV087S531F080X&pf_rd_s=center-1&pf_rd_t=60601&pf_rd_i=whats-on-tv")

    def test_tvshows_top_rated(self):
        main_page = imdb_page.TvshowsTopRated(self.driver)
        menu = imdb_page.Menu(self.driver)
        menu.click_menu_dd()
        main_page.click_top_rated()
        main_page.click_sort_by()
        main_page.click_number_of_ratings()
        main_page.click_enter()
        for i in range(21):
            main_page.page_down()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Learn more about how list ranking is determined.")))
        element.click()
        self.assertEqual(self.driver.current_url, IMDBTVshows.targetURL5)

    def test_tvshows_top_rated_lowest(self):
        main_page = imdb_page.TvshowsTopRated(self.driver)
        menu = imdb_page.Menu(self.driver)
        menu.click_menu_dd()
        main_page.click_top_rated()
        main_page.click_lowest_rated()
        main_page.click_add_to_watchlist()
        assert self.driver.find_element_by_link_text("Create a New Account").text == "Create a New Account"

    def test_tvshows_most_popular(self):
        main_page = imdb_page.TvshowsMostPopular(self.driver)
        menu = imdb_page.Menu(self.driver)
        menu.click_menu_dd()
        main_page.click_most_popular()
        main_page.click_doc()
        main_page.click_runtime()
        main_page.click_next()
        main_page.click_compact()
        self.assertEqual(self.driver.current_url, IMDBTVshows.targetURL6)

    def test_tvshows_most_popular_share(self):
        main_page = imdb_page.TvshowsMostPopular(self.driver)
        menu = imdb_page.Menu(self.driver)
        menu.click_menu_dd()
        main_page.click_most_popular()
        main_page.click_share()
        main_page.click_copy()
        main_page.click_search_field()
        main_page.copy_text()
        main_page.click_search_button()
        assert self.driver.find_element_by_xpath("//h3[contains(.,'Recently Viewed')]").text == "Recently Viewed"

    def test_tvshows_browse_tvshow(self):
        main_page = imdb_page.TvshowsBrowseTvshows(self.driver)
        menu = imdb_page.Menu(self.driver)
        menu.click_menu_dd()
        main_page.click_browse()
        main_page.click_search()
        main_page.click_searchfield()
        main_page.click_go()
        main_page.page_down()
        assert self.driver.find_element_by_link_text("laser-ball").text == "laser-ball"

    def test_tvshows_browse_tvshow_bmovie(self):
        main_page = imdb_page.TvshowsBrowseTvshows(self.driver)
        menu = imdb_page.Menu(self.driver)
        menu.click_menu_dd()
        main_page.click_browse()
        main_page.click_bmovie()
        main_page.choose_year()
        assert self.driver.find_element_by_xpath("//*[@id='main']/div/div[2]/div[3]")

    def test_tvshows_tvnews(self):
        main_page = imdb_page.TvshowsTvnews(self.driver)
        menu = imdb_page.Menu(self.driver)
        menu.click_menu_dd()
        main_page.click_tvnews()
        main_page.click_second_article()
        assert self.driver.find_element_by_xpath("//section[@id='news-article-list']/article[2]/header/h2/a")

    def test_tvshows_tvnews_top(self):
        main_page = imdb_page.TvshowsTvnews(self.driver)
        menu = imdb_page.Menu(self.driver)
        menu.click_menu_dd()
        main_page.click_tvnews()
        main_page.click_top_news()
        self.assertEqual(self.driver.current_url, IMDBTVshows.targetURL7)

    def test_tvshows_indian(self):
        main_page = imdb_page.TvshowsIndian(self.driver)
        menu = imdb_page.Menu(self.driver)
        menu.click_menu_dd()
        main_page.click_indian_tv()
        main_page.click_top_rated()
        main_page.click_see_more()
        main_page.click_descending()
        for i in range(3):
            self.driver.back()
        self.assertEqual(self.driver.current_url, IMDBTVshows.targetURL0)

    def test_tvshows_indian_clear_history(self):
        main_page = imdb_page.TvshowsIndian(self.driver)
        menu = imdb_page.Menu(self.driver)
        menu.click_menu_dd()
        main_page.click_indian_tv()
        main_page.click_most_anticipated()
        main_page.click_second_on_list()
        self.driver.back()
        for i in range(2):
            main_page.page_down()
        main_page.click_clear_history()
        assert self.driver.find_element_by_xpath("//a[contains(text(),'Press Room')]").text == "Press Room"

    def tearDown(self):
        self.driver.close()


class IMDBCreate(unittest.TestCase):

    targetURL8 = "https://www.imdb.com/ap/cvf/verify"

    def setUp(self):
        self.driver = webdriver_factory()
        self.driver.get("https://www.imdb.com/?ref_=nv_home")

    def test_create_user_ascii(self):
        main_page = imdb_page.CreateUser(self.driver)
        main_page.click_sign_in()
        main_page.click_create_account()
        main_page.generate_name_email_ascii()
        main_page.generate_password()
        main_page.create()
        main_page.click_hear_letters()
        main_page.click_play()
        time.sleep(20)
        self.assertEqual(self.driver.current_url, IMDBCreate.targetURL8)

    def test_create_user_chr(self):
        main_page = imdb_page.CreateUser(self.driver)
        main_page.click_sign_in()
        main_page.click_create_account()
        main_page.generate_name_email_chr()
        main_page.generate_password()
        main_page.create()
        assert self.driver.find_element_by_xpath("//a[contains(text(),'Sign-In')]")

    def tearDown(self):
        print("Tearing down test")
        self.driver.close()
