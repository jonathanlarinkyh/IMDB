import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class IMDBTestCase(unittest.TestCase):

    def setUp(self):
        """Skapar en Chrome instans"""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.addCleanup(self.driver.quit)

    def test_whats_new(self):
        """ Testar titeln i 'What to watch'. """
        self.driver.get('https://www.imdb.com')
        self.driver.find_element_by_xpath("//label[@id='imdbHeader-navDrawerOpen--desktop']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[2]/span/div/div/ul/a").click()
        time.sleep(2)
        assert self.driver.find_element_by_css_selector(".ipc-title--page-title > .ipc-title__text").text == "What to Watch"

    def test_latest_trailers(self):
        """ Testar titeln i 'Latest Trailers'. """
        self.driver.get('https://www.imdb.com')
        self.driver.find_element_by_xpath("//label[@id='imdbHeader-navDrawerOpen--desktop']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[2]/span/div/div/ul/a[2]").click()
        time.sleep(2)
        assert self.driver.find_element_by_css_selector(".ipc-title__text").text == "Movie & TV trailers"

    def test_IMDB_Originals(self):
        """ Testar titeln i 'IMDb Originals'. """
        self.driver.get('https://www.imdb.com')
        self.driver.find_element_by_xpath("//label[@id='imdbHeader-navDrawerOpen--desktop']").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("IMDb Originals").click()
        time.sleep(2)
        assert self.driver.find_element_by_css_selector("a > h1").text == "IMDb ORIGINALS"

    def test_IMDB_Picks(self):
        """ Testar titeln i 'IMDb Picks'. """
        self.driver.get('https://www.imdb.com')
        self.driver.find_element_by_xpath("//label[@id='imdbHeader-navDrawerOpen--desktop']").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("IMDb Picks").click()
        time.sleep(2)
        assert self.driver.find_element_by_xpath("//h1").text == "IMDb PICKS"

    def test_IMDB_Podcasts(self):
        """ Testar titeln i 'IMDb Podscasts'. """
        self.driver.get('https://www.imdb.com')
        self.driver.find_element_by_xpath("//label[@id='imdbHeader-navDrawerOpen--desktop']").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("IMDb Podcasts").click()
        time.sleep(2)
        assert self.driver.find_element_by_xpath("//h1").text == "IMDb PODCASTS"
        self.driver.back()
        time.sleep(2)


if __name__ == '__main__':
    unittest.main(verbosity=2)