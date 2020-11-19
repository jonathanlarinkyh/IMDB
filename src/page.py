from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from selenium.webdriver.common.keys import Keys
#s2323jkjk

class PageObject:

    def page_down(self):
        self.driver.find_element_by_tag_name("html").send_keys(Keys.PAGE_DOWN)

    def page_up(self):
        self.driver.find_element_by_tag_name("html").send_keys(Keys.PAGE_UP)


class IMDBMenuMovies(PageObject):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_menu_dd(self):
        self.driver.find_element_by_xpath("//label[@id='imdbHeader-navDrawerOpen--desktop']").click()

    def click_menu_dd_release_calendar(self):
        self.driver.find_element_by_xpath("//a[contains(@href, 'https://www.imdb.com/calendar/?ref_=nv_mv_cal')]").click()

    def click_menu_dd_dvd_blue_releases(self):
        self.driver.find_element_by_xpath("//a[contains(@href, 'https://www.imdb.com/list/ls016522954/?ref_=nv_tvv_dvd')]").click()

    def click_menu_dd_top_rated_movies(self):
        self.driver.find_element_by_xpath("//a[contains(@href, '/chart/top/?ref_=nv_mv_250')]").click()

    def click_menu_dd_most_popular_movies(self):
        self.driver.find_element_by_xpath("//a[contains(@href, '/chart/moviemeter/?ref_=nv_mv_mpm')]").click()

    def click_menu_dd_browse_movies_by_genre(self):
        self.driver.find_element_by_xpath("//a[contains(@href, 'https://www.imdb.com/feature/genre/?ref_=nv_ch_gr')]").click()

    def click_menu_dd_top_box_office(self):
        self.driver.find_element_by_xpath("//a[contains(@href, '/chart/boxoffice/?ref_=nv_ch_cht')]").click()

    def click_menu_dd_showtime_tickets(self):
        self.driver.find_element_by_xpath("//a[contains(@href, 'https://www.imdb.com/showtimes/?ref_=nv_mv_sh')]").click()

    def click_menu_dd_in_theater(self):
        self.driver.find_element_by_xpath("//a[contains(@href, 'https://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth')]").click()
