import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageObject:
    def __init__(self):
        self.driver = webdriver

    def page_down(self):
        self.driver.find_element_by_tag_name("html").send_keys(Keys.PAGE_DOWN)

    def page_up(self):
        self.driver.find_element_by_tag_name("html").send_keys(Keys.PAGE_UP)

    # def accept_cookies(self):
    #     self.driver.find_element_by_id("cn-accept-cookie").click()

    def find_element_clickable_element_by_xpath(self, selector, wait=10):
        return WebDriverWait(self.driver, wait).until(EC.element_to_be_clickable((By.XPATH, selector)))

    def find_element_clickable_element_by_css_selector(self, selector, wait=10):
        return WebDriverWait(self.driver, wait).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))

    def find_visible_element_by_xpath(self, selector, wait=10):
        return WebDriverWait(self.driver, wait).until(EC.visibility_of_element_located((By.XPATH, selector)))


class IMDBMainPage(PageObject):

    def __init__(self, driver: webdriver.Firefox):
        super().__init__()
        self.driver = driver

    def click_menu_dd(self):
        self.find_element_clickable_element_by_xpath("//label[contains(.,'Menu')]", wait=10).click()


class IMDB_menu_community(PageObject):

    def __init__(self, driver: webdriver.Chrome):
        super().__init__()
        self.driver = driver

    def click_menu_dd(self):
        self.find_element_clickable_element_by_xpath("//label[contains(.,'Menu')]", wait=10).click()

    def click_Help_center(self):
        self.find_element_clickable_element_by_xpath("/html/body/div[1]/nav/div[2]/aside/div/div[2]/div/div[6]/span/div/div/ul/a[1]" , wait=10).click()

    def click_contributor_zone(self):
        self.find_element_clickable_element_by_xpath("/html/body/div[1]/nav/div[2]/aside/div/div[2]/div/div[6]/span/div/div/ul/a[2]" , wait=10).click()

    def click_polls(self):
        self.find_element_clickable_element_by_xpath("/html/body/div[1]/nav/div[2]/aside/div/div[2]/div/div[6]/span/div/div/ul/a[3]" , wait=10).click()

        pass