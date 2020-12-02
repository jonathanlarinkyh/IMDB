import unittest
from selenium import webdriver
import page


def web_settings():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()

    return driver


class IMDBTestCase(unittest.TestCase):

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
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)


""" functions = page.PageObject(self.driver)
functions.page_whole_down()
main_page.click_clear_history() """