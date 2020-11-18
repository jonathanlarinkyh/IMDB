
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class PageObject:
    def click_page_down(self):
        self.driver.find_element_by_tag_name("html").send_keys(Keys.PAGE_DOWN)

    def click_page_up(self):
        self.driver.find_element_by_tag_name("html").send_keys(Keys.PAGE_UP)


class KYHMainPage(PageObject):

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_vara_utbildningar_dd(self):
        self.driver.find_element_by_xpath("//nav/div/button").click()

    def click_it_in_dd(self):
        self.driver.find_element_by_link_text("IT").click()

    def click_samhallsbyggnad_in_dd(self):
        pass


class VaraUtbildningar(PageObject):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_goteborg(self):
        self.driver.find_element_by_xpath("//button[contains(.,'Göteborg')]").click()

    def click_distans(self):
        self.driver.find_element_by_xpath("//button[contains(.,'Distans')]").click()

    def click_pvt(self):
        self.driver.find_element_by_xpath("//h3[contains(.,'Programvarutestare')]").click()
        time.sleep(0.5)

    def click_page_down(self):
        self.driver.find_element_by_tag_name("html").send_keys(Keys.PAGE_DOWN)


class OmKyh(PageObject):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_om_kyh_dd(self):
        self.driver.find_element_by_xpath("//div[2]/buttonQQQ").click()

    def click_om_oss(self):
        self.driver.find_element_by_xpath("//a[contains(.,'Om oss')]").click()

    def click_vad_ar_yh_utbildning(self):
        self.driver.find_element_by_link_text("Vad är YH-utbildning?").click()


class KontaktaOss(PageObject):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_kontakta_oss_dd(self):
        self.driver.find_element_by_xpath("//div[3]/button").click()

    def click_kontakta_oss(self):
        self.driver.find_element_by_xpath("//a[contains(.,'Kontakta oss')]").click()

    def click_jag_vill_jobba_hos_er(self):
        self.driver.find_element_by_xpath("//button[contains(.,'Jag vill jobba hos er')]").click()

    def click_lediga_jobb(self):
        self.driver.find_element_by_xpath("//a[contains(.,'lediga jobb')]").click()

class Inspriation(PageObject):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_inspiration_dd(self):
        self.driver.find_element_by_xpath("//div[4]/button").click()

    def click_meny(self):
        self.driver.find_element_by_xpath("//a[contains(.,'Meny')]").click()

    def click_event(self):
        self.driver.find_element_by_xpath("//li[2]/button").click()

    def click_senaste(self):
        self.driver.find_element_by_xpath("//span[contains(.,'Senaste')]").click()


class Antagning(PageObject):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_antagning_dd(self):
        self.driver.find_element_by_xpath("//div[5]/button").click()

    def click_antagning(self):
        self.driver.find_element_by_xpath("//a[contains(.,'Antagning')]").click()

    def click_till_ansokan(self):
        self.driver.find_element_by_xpath("//a/div/div")


