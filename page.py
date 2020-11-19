from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PageObject:
    def __init__(self):
        self.driver = webdriver

    def page_down(self):
        self.driver.find_element_by_tag_name("html").send_keys(Keys.PAGE_DOWN)

    def page_up(self):
        self.driver.find_element_by_tag_name("html").send_keys(Keys.PAGE_UP)

    # def accept_cookies(self):
    #     self.driver.find_element_by_id("cn-accept-cookie").click()


class IMDBMainPage(PageObject):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_menu_dd(self):
        self.driver.find_element_by_xpath("//label[@id='imdbHeader-navDrawerOpen--desktop']").click()


class IMDB_menu_awards(PageObject):

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_oscars(self):
        self.driver.find_element_by_link_text("Oscars").click()


class imdb(PageObject):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
