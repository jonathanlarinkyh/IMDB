from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#s2323jkjk


class PageObject:

    def page_down(self):
        self.driver.find_element_by_tag_name("html").send_keys(Keys.PAGE_DOWN)

    def page_up(self):
        self.driver.find_element_by_tag_name("html").send_keys(Keys.PAGE_UP)

    def page_whole_down(self):
        for page in range(0, 6):
            self.driver.find_element_by_tag_name("html").send_keys(Keys.PAGE_DOWN)

    def page_whole_up(self):
        for page in range(0, 6):
            self.driver.find_element_by_tag_name("html").send_keys(Keys.PAGE_UP)

    def find_element_click_element_by_xpath(self, selector, wait=0):
        return WebDriverWait(self.driver, wait).until(EC.element_to_be_clickable((By.XPATH, selector)))

    def find_element_click_element_by_css_selector(self, selector, wait=0):
        return WebDriverWait(self.driver, wait).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))


class IMDBMenuMovies(PageObject):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_home(self):
        self.driver.find_element_by_xpath("(//a[contains(@href, '/?ref_=nv_home')])[2]").click()

    def click_menu_dd(self):
        self.find_element_click_element_by_xpath("//label[@id='imdbHeader-navDrawerOpen--desktop']", wait=10).click()

    def click_menu_dd_release_calendar(self):
        self.find_element_click_element_by_xpath("//a[contains(@href, 'https://www.imdb.com/calendar/?ref_=nv_mv_cal')]", wait=10).click()

    def click_menu_dd_dvd_blue_releases(self):
        self.find_element_click_element_by_xpath("//a[contains(@href, 'https://www.imdb.com/list/ls016522954/?ref_=nv_tvv_dvd')]", wait=10).click()

    def click_menu_dd_top_rated_movies(self):
        self.find_element_click_element_by_xpath("//a[contains(@href, '/chart/top/?ref_=nv_mv_250')]", wait=10).click()

    def click_menu_dd_most_popular_movies(self):
        self.find_element_click_element_by_xpath("//a[contains(@href, '/chart/moviemeter/?ref_=nv_mv_mpm')]", wait=10).click()

    def click_menu_dd_browse_movies_by_genre(self):
        self.find_element_click_element_by_xpath("//a[contains(@href, 'https://www.imdb.com/feature/genre/?ref_=nv_ch_gr')]", wait=10).click()

    def click_menu_dd_top_box_office(self):
        self.find_element_click_element_by_xpath("//a[contains(@href, '/chart/boxoffice/?ref_=nv_ch_cht')]", wait=10).click()

    def click_menu_dd_showtime_tickets(self):
        self.find_element_click_element_by_xpath("//a[contains(@href, 'https://www.imdb.com/showtimes/?ref_=nv_mv_sh')]", wait=10).click()

    def click_menu_dd_in_theater(self):
        self.find_element_click_element_by_xpath("//a[contains(@href, 'https://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth')]", wait=10).click()

    def click_menu_dd_coming_soon(self):
        self.find_element_click_element_by_xpath("//a[contains(@href, 'https://www.imdb.com/coming-soon/?ref_=nv_mv_cs')]", wait=10).click()

    def click_menu_dd_movie_news(self):
        self.find_element_click_element_by_xpath("//a[contains(.,'Movie News')]", wait=10).click()

    def click_menu_dd_india_movie_spotlight(self):
        self.find_element_click_element_by_xpath("//a[contains(.,'India Movie Spotlight')]", wait=10).click()


class ReleaseCalendar(PageObject):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_clear_history(self):
        self.find_element_click_element_by_css_selector("#clear_rvi", wait=10).click()

    def click_first_choice(self):
        self.find_element_click_element_by_css_selector("#main > ul:nth-child(2) a", wait=10).click()

    def click_second_choice(self):
        self.find_element_click_element_by_css_selector("ul:nth-child(4) > li:nth-child(1) > a", wait=10).click()

    def click_director(self):
        self.find_element_click_element_by_css_selector(".credit_summary_item:nth-child(2) > a", wait=10).click()
