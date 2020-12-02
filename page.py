from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class PageObject:
    def back_page(self):
        self.driver.find_element_by_tag_name("html").send_keys(Keys.BACK_SPACE)

    def page_down(self):
        self.driver.find_element_by_tag_name("html").send_keys(Keys.PAGE_DOWN)

    def page_up(self):
        self.driver.find_element_by_tag_name("html").send_keys(Keys.PAGE_UP)

    def page_whole_down(self):
        for page in range(0, 8):
            self.driver.find_element_by_tag_name("html").send_keys(Keys.PAGE_DOWN)

    def page_whole_up(self):
        for page in range(0, 6):
            self.driver.find_element_by_tag_name("html").send_keys(Keys.PAGE_UP)

    def find_element_click_element_by_xpath(self, selector, wait=0):
        return WebDriverWait(self.driver, wait).until(EC.element_to_be_clickable((By.XPATH, selector)))

    def find_element_click_element_by_css_selector(self, selector, wait=0):
        return WebDriverWait(self.driver, wait).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))

    def find_element_visible_element_by_xpath(self, selector, wait=0):
        return WebDriverWait(self.driver, wait).until(EC.visibility_of_element_located((By.XPATH, selector)))


class IMDBMenuWatch(PageObject):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_home(self):
        self.driver.find_element_by_xpath("(//a[contains(@href, '/?ref_=nv_home')])[2]").click()

    def click_dd_menu(self):
        self.find_element_click_element_by_xpath("//label[@id='imdbHeader-navDrawerOpen--desktop']", wait=10).click()

    def click_clear_history(self):
        self.find_element_click_element_by_css_selector("#clear_rvi", wait=10).click()

    def click_dd_menu_whats_new(self):
        self.find_element_click_element_by_xpath("//a[contains(@href, '/what-to-watch/?ref_=nv_watch')]", wait=10).click()

    def click_dd_menu_latest_trailers(self):
        self.find_element_click_element_by_xpath("//a[contains(@href, '/trailers/?ref_=nv_mv_tr')]", wait=10).click()

    def click_dd_menu_originals(self):
        self.find_element_click_element_by_xpath("//a[contains(@href, '/originals/?ref_=nv_sf_ori')]", wait=10).click()

    def click_dd_menu_picks(self):
        self.find_element_click_element_by_xpath("//a[contains(@href, '/imdbpicks/?ref_=nv_pi')]", wait=10).click()

    def click_dd_menu_podcasts(self):
        self.find_element_click_element_by_xpath("//a[contains(@href, '/podcasts/?ref_=nv_pod')]", wait=20).click()


class IMDBWhatToWatch(PageObject):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_most_popular(self):
        self.find_element_click_element_by_xpath("//li[5]/span", wait=10).click()

    def click_fan_favorites(self):
        self.find_element_click_element_by_css_selector(".ipc-tab:nth-child(2) > span", wait=10).click()

    def click_10th_choice(self):
        self.find_element_click_element_by_xpath("//div[10]/div[3]/button/div", wait=10).click()

