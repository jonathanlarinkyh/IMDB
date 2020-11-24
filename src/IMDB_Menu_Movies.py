import unittest

from selenium import webdriver
import time
from IMDB.src import page


#Sweet

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
        time.sleep(1)
        main_page.click_menu_dd_release_calendar()
        self.assertEqual(self.driver.current_url, "https://www.imdb.com/calendar/?ref_=nv_mv_cal")

    def test_dvd_blue_releases_in_dd(self):
        main_page = page.IMDBMenuMovies(self.driver)
        main_page.click_menu_dd()
        time.sleep(1)
        main_page.click_menu_dd_dvd_blue_releases()
        self.assertEqual(self.driver.current_url, "https://www.imdb.com/list/ls016522954/?ref_=nv_tvv_dvd")

    def test_top_rated_movies_in_dd(self):
        main_page = page.IMDBMenuMovies(self.driver)
        main_page.click_menu_dd()
        time.sleep(1)
        main_page.click_menu_dd_top_rated_movies()

    def test_most_popular_movies_in_dd(self):
        main_page = page.IMDBMenuMovies(self.driver)
        main_page.click_menu_dd()
        time.sleep(1)
        main_page.click_menu_dd_most_popular_movies()

    def test_browse_movies_by_genre_in_dd(self):
        main_page = page.IMDBMenuMovies(self.driver)
        main_page.click_menu_dd()
        time.sleep(1)
        main_page.click_menu_dd_browse_movies_by_genre()

    def test_top_box_office_in_dd(self):
        main_page = page.IMDBMenuMovies(self.driver)
        main_page.click_menu_dd()
        time.sleep(1)
        main_page.click_menu_dd_top_box_office()

    def test_showtime_tickets_in_dd(self):
        main_page = page.IMDBMenuMovies(self.driver)
        main_page.click_menu_dd()
        time.sleep(1)
        main_page.click_menu_dd_showtime_tickets()

    def test_in_theaters_in_dd(self):
        main_page = page.IMDBMenuMovies(self.driver)
        main_page.click_menu_dd()
        time.sleep(1)
        main_page.click_menu_dd_in_theater()

    def tearDown(self):
        self.driver.close()


class IMDBReleaseCalendar(unittest.TestCase):

    def setUp(self):
        self.driver = web_factory()
        self.driver.get("https://www.imdb.com/")

    def test_release_calendar_movie_clear(self):
        main_page = page.IMDBMenuMovies(self.driver)
        main_page.click_menu_dd()
        time.sleep(1)
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
        time.sleep(1)
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

    def test_click_director(self):
        main_page = page.IMDBMenuMovies(self.driver)
        main_page.click_menu_dd()
        time.sleep(1)
        main_page.click_menu_dd_release_calendar()

        second_page = page.ReleaseCalendar(self.driver)
        second_page.click_first_choice()
        time.sleep(1)
        second_page.click_director()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)