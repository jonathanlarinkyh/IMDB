from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PageObject:
    def page_down(self):
        self.driver.find_element_by_tag_name("html").send_keys(Keys.PAGE_DOWN)

    def page_up(self):
        self.driver.find_element_by_tag_name("html").send_keys(Keys.PAGE_UP)

    def accept_cookies(self):
        self.driver.find_element_by_id("cn-accept-cookie").click()


class IMDBMainPage(PageObject):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver


        pass