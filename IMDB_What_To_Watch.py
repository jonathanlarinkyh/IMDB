import unittest
from selenium import webdriver
import time
from datetime import datetime
import page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
import HtmlTestRunner


def web_settings():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()

    return driver


class IMDBNavTestCase(unittest.TestCase):

    def setUp(self):
        """ Startar testen från IMDB startsida. """
        self.driver = web_settings()
        self.driver.get("https://www.imdb.com")

    def test_drop_down_menu(self):
        """ Testar dropdown-menu från startsidan. """
        main_page = page.IMDBMenuWatch(self.driver)
        main_page.click_dd_menu()

    def test_whats_new(self):
        """ Testar titeln i 'What to watch'. """
        main_page = page.IMDBMenuWatch(self.driver)
        main_page.click_dd_menu()
        main_page.click_dd_menu_whats_new()
        self.assertEqual(self.driver.current_url, "https://www.imdb.com/what-to-watch/?ref_=nv_watch")

    def test_latest_trailers(self):
        """ Testar titeln i 'Latest Trailers'. """
        main_page = page.IMDBMenuWatch(self.driver)
        main_page.click_dd_menu()
        main_page.click_dd_menu_latest_trailers()
        self.assertEqual(self.driver.current_url, "https://www.imdb.com/trailers/?ref_=nv_mv_tr")

    def test_originals(self):
        """ Testar titeln i 'IMDb Originals'. """
        main_page = page.IMDBMenuWatch(self.driver)
        main_page.click_dd_menu()
        main_page.click_dd_menu_originals()
        self.assertEqual(self.driver.current_url, "https://www.imdb.com/originals/?ref_=nv_sf_ori")

    def test_picks(self):
        """ Testar titeln i 'IMDb Picks'. """
        main_page = page.IMDBMenuWatch(self.driver)
        main_page.click_dd_menu()
        main_page.click_dd_menu_picks()
        self.assertEqual(self.driver.current_url, "https://www.imdb.com/imdbpicks/?ref_=nv_pi")

    def test_podcasts(self):
        """ Testar titeln i 'IMDb Podscasts'. """
        main_page = page.IMDBMenuWatch(self.driver)
        main_page.click_dd_menu()
        main_page.click_dd_menu_podcasts()
        self.assertEqual(self.driver.current_url, "https://www.imdb.com/podcasts/?ref_=nv_pod")

    def tearDown(self):
        date = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        file_name = 'reports/report_pic-%s.png' % date
        self.driver.get_screenshot_as_file(file_name)
        self.driver.quit()


class IMDBWhatToWatchTestCase(unittest.TestCase):

    def setUp(self):
        """ Startar testen från IMDB startsida. """
        self.driver = web_settings()
        self.driver.get("https://www.imdb.com")

    def test_what_to_watch(self):
        """ Testar navigation i ' What to watch' """
        main_page = page.IMDBMenuWatch(self.driver)
        second_page = page.IMDBWhatToWatch(self.driver)

        main_page.click_dd_menu()
        main_page.click_dd_menu_whats_new()
        second_page.click_fan_favorites()
        time.sleep(3)
        main_page.page_whole_down()
        time.sleep(1)
        main_page.page_whole_up()
        second_page.click_most_popular()
        time.sleep(2)

    def test_clear_history(self):
        """ Testar att cleara historiken efter val av film """
        main_page = page.IMDBMenuWatch(self.driver)
        second_page = page.IMDBWhatToWatch(self.driver)

        main_page.click_dd_menu()
        main_page.click_dd_menu_whats_new()
        second_page.click_first_choice()
        second_page.pick_first_movie()
        time.sleep(1)
        self.driver.back()
        main_page.page_whole_down()
        time.sleep(2)
        second_page.click_clear_history()
        time.sleep(2)

    def tearDown(self):
        date = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        file_name = 'reports/report_pic-%s.png' % date
        self.driver.get_screenshot_as_file(file_name)

        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_name="FullReport",
                                                           template="template_report/reports.html",
                                                           add_timestamp=False), verbosity=2)