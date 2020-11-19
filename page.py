from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


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

    def click_menu_dd(self):
        self.driver.find_element_by_xpath("//label[@id='imdbHeader-navDrawerOpen--desktop']").click()

    def click_oscars(self):
        self.driver.find_element_by_xpath("//a[@href='/oscars/?ref_=nv_ev_acd']").click()

    def click_best_picture_Winner(self):
        self.driver.find_element_by_xpath("//*[@id='imdbHeader']/div[2]/aside/div/div[2]/div/div["
                                          "3]/span/div/div/ul/a[3]").click()

    def click_Golden_Globes(self):
        self.driver.find_element_by_xpath("//a[@href='/golden-globes/?ref_=nv_ev_gg']").click()
    #

    def click_Emmys(self):
        self.driver.find_element_by_xpath("//a[@href='/emmys/?ref_=nv_ev_rte']").click()
    #

    def click_STARmeter_Awards(self):
        self.driver.find_element_by_xpath("//a[@href='/starmeterawards/?ref_=nv_ev_sma']").click()
    #

    def click_SanDiego_Comic_Con(self):
        self.driver.find_element_by_xpath("//a[@href='/comic-con/?ref_=nv_ev_comic']").click()
    #

    def click_NY_Comic_Con(self):
        self.driver.find_element_by_xpath("//a[@href='/nycc/?ref_=nv_ev_nycc']").click()
    #

    def click_Sundance_Film_Festival(self):
        self.driver.find_element_by_xpath("//a[@href='/sundance/?ref_=nv_ev_sun']").click()
    #

    def click_Toronto_Intl_Film_Festival(self):
        self.driver.find_element_by_xpath("//a[@href='/toronto/?ref_=nv_ev_tor']").click()
    #

    def click_Awards_central(self):
        self.driver.find_element_by_xpath("//a[@href='/awards-central/?ref_=nv_ev_awrd']").click()
    #

    def click_Festival_Central(self):
        self.driver.find_element_by_xpath("//a[@href='/festival-central/?ref_=nv_ev_fc']").click()
    #

    def click_All_Events(self):
        self.driver.find_element_by_xpath("//a[@href='https://www.imdb.com/event/all/?ref_=nv_ev_all']").click()





class imdb(PageObject):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
