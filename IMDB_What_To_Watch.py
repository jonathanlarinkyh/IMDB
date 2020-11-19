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
        time.sleep(3)


if __name__ == '__main__':
    unittest.main(verbosity=2)