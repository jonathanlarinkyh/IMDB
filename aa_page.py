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

    def find_element_clickable_element_by_xpath(self, selector, wait=0):
        return WebDriverWait(self.driver, wait).until(EC.element_to_be_clickable((By.XPATH, selector)))

    def find_element_clickable_element_by_css_selector(self, selector, wait=0):
        return WebDriverWait(self.driver, wait).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))

    def find_visible_element_by_xpath(self, selector, wait=0):
        return WebDriverWait(self.driver, wait).until(EC.visibility_of_element_located((By.XPATH, selector)))


class IMDBMainPage(PageObject):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__()
        self.driver = driver

    def click_menu_dd(self):
        self.find_element_clickable_element_by_xpath("//label[contains(.,'Menu')]", wait=10).click()
        self.driver.save_screenshot("SC_Amaj/Menu/" + "Menu_SC " + time.asctime().replace(":", "") + ".png")


class IMDB_menu_awards(PageObject):

    def __init__(self, driver: webdriver.Chrome):
        super().__init__()
        self.driver = driver

    def click_menu_dd(self):
        self.find_element_clickable_element_by_xpath("//label[contains(.,'Menu')]", wait=10).click()

    def click_oscars(self):
        self.find_element_clickable_element_by_xpath("//a[@href='/oscars/?ref_=nv_ev_acd']", wait=15).click()
        self.driver.save_screenshot("SC_Amaj/Oscars/" + "OSCAR_SC " + time.asctime().replace(":", "") + ".png")
        time.sleep(5)

        self.find_element_clickable_element_by_css_selector(" a[title='Winners'] span:nth-child(1)").click()
        self.driver.save_screenshot("SC_Amaj/Oscars/" + "Winners_SC " + time.asctime().replace(":", "") + ".png")
        time.sleep(5)

    def click_best_picture_Winner(self):
        self.find_element_clickable_element_by_xpath("//*[@id='imdbHeader']/div[2]/aside/div/div[2]/div/div[3]/span/div/div/ul/a[3]", wait=15).click()
        self.driver.save_screenshot("SC_Amaj/BPW/" + "BPW_SC" + time.asctime().replace(":", "") + ".png")

    def click_Golden_Globes(self):
        self.find_element_clickable_element_by_xpath("//a[@href='/golden-globes/?ref_=nv_ev_gg']", wait=15).click()
        self.driver.save_screenshot("SC_Amaj/G-Globes/" + "Golden Globe " + time.asctime().replace(":", "") + ".png")

    #

    def click_Emmys(self):
        self.find_element_clickable_element_by_xpath("//a[@href='/emmys/?ref_=nv_ev_rte']", wait=15).click()
        self.driver.save_screenshot("SC_Amaj/Emmys/" + "Emmys_SC" + time.asctime().replace(":", "") + ".png")

    #

    def click_STARmeter_Awards(self):
        self.find_element_clickable_element_by_xpath("//a[@href='/starmeterawards/?ref_=nv_ev_sma']", wait=15).click()
        self.driver.save_screenshot("SC_Amaj/Star Meter Awards/" + "StarMeter Awards " + time.asctime().replace(":", "") + ".png")

    #

    def click_SanDiego_Comic_Con(self):
        self.find_element_clickable_element_by_xpath("//a[@href='/comic-con/?ref_=nv_ev_comic']", wait=15).click()
        self.driver.save_screenshot("SC_Amaj/SD Comic-Con/" + "SD_Comic_Con " + time.asctime().replace(":", "") + ".png")

    #

    def click_NY_Comic_Con(self):
        self.find_element_clickable_element_by_xpath("//a[@href='/nycc/?ref_=nv_ev_nycc']", wait=15).click()
        self.driver.save_screenshot("SC_Amaj/NY Comic-Con/" + "NY Comic_Con " + time.asctime().replace(":", "") + ".png")

    #

    def click_Sundance_Film_Festival(self):
        self.find_element_clickable_element_by_xpath("//a[@href='/sundance/?ref_=nv_ev_sun']", wait=15).click()
        self.driver.save_screenshot("SC_Amaj/Sundance Film F/" + "Sundance Film Fes " + time.asctime().replace(":", "") + ".png")

    #

    def click_Toronto_Intl_Film_Festival(self):
        self.find_element_clickable_element_by_xpath("//a[@href='/toronto/?ref_=nv_ev_tor']", wait=15).click()
        self.driver.save_screenshot("SC_Amaj/Toronto Intl Film F/" + "Toronto Intl FF " + time.asctime().replace(":", "") + ".png")
        time.sleep(5)

    #

    def click_Awards_central(self):
        self.find_element_clickable_element_by_xpath("//a[@href='/awards-central/?ref_=nv_ev_awrd']", wait=15).click()
        self.driver.save_screenshot("SC_Amaj/Awards Central/" + "Awards Central " + time.asctime().replace(":", "") + ".png")

    #

    def click_Festival_Central(self):
        self.find_element_clickable_element_by_xpath("//a[@href='/festival-central/?ref_=nv_ev_fc']", wait=15).click()
        self.driver.save_screenshot("SC_Amaj/Festival Central/" + "Festival Central " + time.asctime().replace(":", "") + ".png")

    #

    def click_All_Events(self):
        self.find_element_clickable_element_by_xpath("//a[@href='https://www.imdb.com/event/all/?ref_=nv_ev_all']", wait=15).click()
        self.driver.save_screenshot("SC_Amaj/All Events/" + "All Events " + time.asctime().replace(":", "") + ".png")


class IMDB_Menu_Oscars(PageObject):

    def __init__(self, driver: webdriver.Chrome):
        super().__init__()
        self.driver = driver

    def click_oscars_menu(self):
        self.find_element_clickable_element_by_xpath("//label[contains(.,'Menu')]", wait=10).click()

    def click_oscars_main(self):
        self.find_element_clickable_element_by_xpath("//a[@href='/oscars/?ref_=nv_ev_acd']", wait=15).click()
        time.sleep(5)

    def click_winners_in_oscar(self):
        self.find_element_clickable_element_by_css_selector(" a[title='Winners'] span:nth-child(1)").click()
        self.driver.save_screenshot("SC_Amaj/Oscars/" + "Winners_SC " + time.asctime().replace(":", "") + ".png")
        time.sleep(5)

    def click_year_in_winners(self):
        self.find_element_clickable_element_by_xpath("//a[normalize-space()='2020']", wait=10).click()
        time.sleep(5)
