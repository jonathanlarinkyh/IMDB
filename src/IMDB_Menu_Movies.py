import unittest

from selenium import webdriver
import time
from IMDB.src import page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException


# Sweet

def web_factory():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()

    return driver


class IMDBPageMenu(unittest.TestCase):

    def _foo(self):
        pass

    def setUp(self):
        self.driver = web_factory()
        self.driver.get("https://www.imdb.com/")

    def test_nav_through_drop_down_menu(self):
        main_page = page.IMDBMenuMovies(self.driver)
        main_page.click_menu_dd()

    def test_release_calendar_in_dd(self):
        main_page = page.IMDBMenuMovies(self.driver)
        main_page.click_menu_dd()
        main_page.click_menu_dd_release_calendar()
        self.assertEqual(self.driver.current_url, "https://www.imdb.com/calendar/?ref_=nv_mv_cal")

    def test_dvd_blue_releases_in_dd(self):
        main_page = page.IMDBMenuMovies(self.driver)
        main_page.click_menu_dd()
        main_page.click_menu_dd_dvd_blue_releases()
        self.assertEqual(self.driver.current_url, "https://www.imdb.com/list/ls016522954/?ref_=nv_tvv_dvd")

    def test_top_rated_movies_in_dd(self):
        main_page = page.IMDBMenuMovies(self.driver)
        main_page.click_menu_dd()
        main_page.click_menu_dd_top_rated_movies()
        self.assertEqual(self.driver.current_url, "https://www.imdb.com/chart/top/?ref_=nv_mv_250")

    def test_most_popular_movies_in_dd(self):
        main_page = page.IMDBMenuMovies(self.driver)
        main_page.click_menu_dd()
        main_page.click_menu_dd_most_popular_movies()
        self.assertEqual(self.driver.current_url, "https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm")

    def test_browse_movies_by_genre_in_dd(self):
        main_page = page.IMDBMenuMovies(self.driver)
        main_page.click_menu_dd()
        main_page.click_menu_dd_browse_movies_by_genre()
        self.assertEqual(self.driver.current_url, "https://www.imdb.com/feature/genre/?ref_=nv_ch_gr")

    def test_top_box_office_in_dd(self):
        main_page = page.IMDBMenuMovies(self.driver)
        main_page.click_menu_dd()
        main_page.click_menu_dd_top_box_office()
        self.assertEqual(self.driver.current_url, "https://www.imdb.com/chart/boxoffice/?ref_=nv_ch_cht")

    def test_showtime_tickets_in_dd(self):
        main_page = page.IMDBMenuMovies(self.driver)
        main_page.click_menu_dd()
        main_page.click_menu_dd_showtime_tickets()
        self.assertEqual(self.driver.current_url, "https://www.imdb.com/showtimes/?ref_=nv_mv_sh")

    def test_in_theaters_in_dd(self):
        main_page = page.IMDBMenuMovies(self.driver)
        main_page.click_menu_dd()
        main_page.click_menu_dd_in_theater()
        self.assertEqual(self.driver.current_url, "https://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth")

    def test_coming_soon_in_dd(self):
        main_page = page.IMDBMenuMovies(self.driver)
        main_page.click_menu_dd()
        main_page.click_menu_dd_coming_soon()
        self.assertEqual(self.driver.current_url, "https://www.imdb.com/movies-coming-soon/?ref_=nv_mv_cs")

    def test_movie_news_in_dd(self):
        main_page = page.IMDBMenuMovies(self.driver)
        main_page.click_menu_dd()
        main_page.click_menu_dd_movie_news()
        self.assertEqual(self.driver.current_url, "https://www.imdb.com/news/movie/?ref_=nv_nw_mv")

    def test_india_movie_spotlight_in_dd(self):
        main_page = page.IMDBMenuMovies(self.driver)
        main_page.click_menu_dd()
        main_page.click_menu_dd_india_movie_spotlight()
        self.assertEqual(self.driver.current_url, "https://www.imdb.com/india/toprated/?ref_=nv_mv_in")

    def tearDown(self):
        self.driver.close()


class IMDBReleaseCalendar(unittest.TestCase):

    def setUp(self):
        self.driver = web_factory()
        self.driver.get("https://www.imdb.com/")

    def test_release_calendar_movie_clear(self):
        main_page = page.IMDBMenuMovies(self.driver)
        main_page.click_menu_dd()
        main_page.click_menu_dd_release_calendar()
        second_page = page.ReleaseCalendar(self.driver)
        second_page.click_first_choice()
        time.sleep(5)
        main_page.page_whole_down()
        time.sleep(5)
        second_page.click_clear_history()
        time.sleep(5)

    def test_release_calendar_movies_clear(self):
        main_page = page.IMDBMenuMovies(self.driver)
        main_page.click_menu_dd()
        main_page.click_menu_dd_release_calendar()

        second_page = page.ReleaseCalendar(self.driver)
        second_page.click_first_choice()
        time.sleep(1)
        main_page.click_home()
        main_page.click_menu_dd()
        main_page.click_menu_dd_release_calendar()
        time.sleep(1)
        second_page.click_second_choice()
        time.sleep(1)
        main_page.page_whole_down()
        time.sleep(1)
        second_page.click_clear_history()

    def test_click_director_clear(self):
        main_page = page.IMDBMenuMovies(self.driver)
        main_page.click_menu_dd()
        main_page.click_menu_dd_release_calendar()

        second_page = page.ReleaseCalendar(self.driver)
        second_page.click_first_choice()
        time.sleep(1)
        second_page.click_director()
        time.sleep(1)
        main_page.page_whole_down()
        second_page.click_clear_history()

    def test_release_calendar_movie_history_clickable(self): #need to check why it works and not
        main_page = page.IMDBMenuMovies(self.driver)
        main_page.click_menu_dd()
        main_page.click_menu_dd_release_calendar()
        second_page = page.ReleaseCalendar(self.driver)
        second_page.click_first_choice()
        time.sleep(1)
        main_page.page_whole_down()
        time.sleep(1)
        second_page.history_clickable_first_image()

    def tearDown(self):
        self.driver.close()


class IMDBDVDnBlueRayReleases(unittest.TestCase):
    def setUp(self):
        self.driver = web_factory()
        self.driver.get("https://www.imdb.com/")

    def test_dvd_blue_click_first_choice(self):
        main_page = page.IMDBMenuMovies(self.driver)
        main_page.click_menu_dd()
        main_page.click_menu_dd_dvd_blue_releases()

        second_page = page.DVDnBlue(self.driver)
        second_page.click_first_choice()

    def test_dvd_blue_click_director(self):
        main_page = page.IMDBMenuMovies(self.driver)
        main_page.click_menu_dd()
        main_page.click_menu_dd_dvd_blue_releases()

        second_page = page.DVDnBlue(self.driver)
        second_page.click_first_choice()
        second_page = page.ReleaseCalendar(self.driver)
        second_page.click_director()

    def test_dvd_blue_click_director_clear(self):
        main_page = page.IMDBMenuMovies(self.driver)
        main_page.click_menu_dd()
        main_page.click_menu_dd_dvd_blue_releases()

        second_page = page.DVDnBlue(self.driver)
        second_page.click_first_choice()
        second_page = page.ReleaseCalendar(self.driver)
        second_page.click_director()
        time.sleep(3)
        main_page.page_whole_down()
        second_page.click_clear_history()

    def test_dvd_blue_history_first_click(self):
        main_page = page.IMDBMenuMovies(self.driver)
        main_page.click_menu_dd()
        main_page.click_menu_dd_dvd_blue_releases()

        second_page = page.DVDnBlue(self.driver)
        second_page.click_first_choice()
        second_page = page.ReleaseCalendar(self.driver)
        time.sleep(3)
        main_page.page_whole_down()
        time.sleep(1)
        second_page.history_clickable_first_image()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)
