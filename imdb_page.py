import random
import string
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# User Generator
letters = [random.choice(string.ascii_lowercase) for l in
           range(random.randint(5, 26))]
password = [random.choice(string.ascii_lowercase) for p in
            range(random.randint(5, 26))]
letters2 = [random.choice(chr(random.randint(0, 65000))) for l2 in
            range(random.randint(5, 26))]
# Email service
emaillist = ["@hotmail.com", "@gmail.com", "@yahoo.com", "@mail.com"]
email = [random.choice(emaillist)]


class PageObject:
    def __init__(self):
        self.driver = webdriver

    def page_down(self):
        self.driver.find_element_by_tag_name("html").send_keys(Keys.PAGE_DOWN)

    def page_up(self):
        self.driver.find_element_by_tag_name("html").send_keys(Keys.PAGE_UP)

    def click_enter(self):
        self.driver.find_element_by_tag_name("html").send_keys(Keys.ENTER)

    def click_backspace(self):
        self.driver.find_element_by_tag_name("html").send_keys(Keys.BACK_SPACE)

    def click_back_page(self):
        self.driver.back()

    def click_forward_page(self):
        self.driver.forward()

    def page_whole_down(self):
        for page in range(0, 8):
            self.driver.find_element_by_tag_name("html").send_keys(Keys.PAGE_DOWN)

    def page_whole_up(self):
        for page in range(0, 8):
            self.driver.find_element_by_tag_name("html").send_keys(Keys.PAGE_UP)

    # def accept_cookies(self):
    #     self.driver.find_element_by_id("cn-accept-cookie").click()

    def find_element_clickable_element_by_xpath(self, selector, wait=10):
        return WebDriverWait(self.driver, wait).until(EC.element_to_be_clickable((By.XPATH, selector)))

    def find_element_clickable_element_by_css_selector(self, selector, wait=10):
        return WebDriverWait(self.driver, wait).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))

    def find_visible_element_by_xpath(self, selector, wait=10):
        return WebDriverWait(self.driver, wait).until(EC.visibility_of_element_located((By.XPATH, selector)))

    def find_element_visible_element_by_link_text(self, selector, wait=0):
        return WebDriverWait(self.driver, wait).until(EC.visibility_of_element_located((By.LINK_TEXT, selector)))

    def find_element_wait_for_element_by_xpath(self, selector, wait=0):
        return WebDriverWait(self.driver, wait).until(EC.element_to_be_clickable((By.XPATH, selector)))


class IMDBMainPage(PageObject):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__()
        self.driver = driver

    def home_page(self):
        self.find_element_clickable_element_by_xpath("//a[@id='home_img_holder']", wait=10).click()

    def click_menu_dd(self):
        self.find_element_clickable_element_by_xpath("//label[contains(.,'Menu')]", wait=10).click()

    def click_browse_trailers(self):
        self.find_element_clickable_element_by_xpath("//a[normalize-space()='Browse trailers']", wait=10).click()

    def click_top_picks(self):
        self.find_element_clickable_element_by_xpath("//*[@id='__next']/main/div[2]/section/section/section/div[1]/ul/li[3]/span", wait=20).click()

    def click_fan_favorite(self):
        self.find_element_clickable_element_by_xpath("//h3[normalize-space()='Fan favorites']", wait=10).click()


class CreateUser(PageObject):

    def __init__(self, driver: webdriver.Chrome):
        super().__init__()
        self.driver = driver

    def click_sign_in(self):
        self.driver.find_element_by_xpath("//nav[@id='imdbHeader']/div[2]/div[5]/a/div").click()

    def click_create_account(self):
        self.driver.find_element_by_link_text("Create a New Account").click()

    def generate_name_email_ascii(self):
        self.driver.find_element_by_xpath("//input[@id='ap_customer_name']").send_keys(letters)
        self.driver.find_element_by_xpath("//input[@id='ap_email']").send_keys(letters + email)

    def generate_name_email(self):
        self.driver.find_element_by_xpath("//input[@id='ap_customer_name']").send_keys(letters2)
        self.driver.find_element_by_xpath("//input[@id='ap_email']").send_keys(letters2 + email)

    def generate_password(self):
        self.driver.find_element_by_css_selector("#ap_password").send_keys(password)
        self.driver.find_element_by_css_selector("#ap_password_check").send_keys(password)
        print("".join(password))

    def create(self):
        self.driver.find_element_by_xpath("//input[@id='continue']").click()

    def change_otp_method(self):
        self.find_element_clickable_element_by_xpath("//a[normalize-space()='(Change)']", wait=10).click()

    def click_hear_letters(self):
        self.driver.find_element_by_xpath("//a[contains(text(),'Hear the characters')]").click()

    def click_play(self):
        self.driver.find_element_by_xpath("//*[@id='cvf-page-content']/div/div/div/div[2]/div/audio").send_keys(Keys.ENTER)

    def find_signin(self):
        self.driver.find_element_by_xpath("//*[@id='cvf-page-content']/div/div")


class IMDB_menu_awards(PageObject):

    def __init__(self, driver: webdriver.Chrome):
        super().__init__()
        self.driver = driver

    def home_page(self):
        self.find_element_clickable_element_by_xpath("//a[@id='home_img_holder']", wait=10).click()

    def click_menu_dd(self):
        self.find_element_clickable_element_by_xpath("//label[contains(.,'Menu')]", wait=10).click()

    def click_oscars(self):
        self.find_element_clickable_element_by_xpath("//a[@href='/oscars/?ref_=nv_ev_acd']", wait=15).click()
        time.sleep(5)

        self.find_element_clickable_element_by_css_selector(" a[title='Winners'] span:nth-child(1)").click()
        time.sleep(5)

    def click_best_picture_Winner(self):
        self.find_element_clickable_element_by_xpath("//*[@id='imdbHeader']/div[2]/aside/div/div[2]/div/div[3]/span/div/div/ul/a[3]", wait=15).click()

    def click_Golden_Globes(self):
        self.find_element_clickable_element_by_xpath("//a[@href='/golden-globes/?ref_=nv_ev_gg']", wait=15).click()

    #

    def click_Emmys(self):
        self.find_element_clickable_element_by_xpath("//a[@href='/emmys/?ref_=nv_ev_rte']", wait=15).click()

    #

    def click_STARmeter_Awards(self):
        self.find_element_clickable_element_by_xpath("//a[@href='/starmeterawards/?ref_=nv_ev_sma']", wait=15).click()

    #

    def click_SanDiego_Comic_Con(self):
        self.find_element_clickable_element_by_xpath("//a[@href='/comic-con/?ref_=nv_ev_comic']", wait=15).click()

    #

    def click_NY_Comic_Con(self):
        self.find_element_clickable_element_by_xpath("//a[@href='/nycc/?ref_=nv_ev_nycc']", wait=15).click()

    #

    def click_Sundance_Film_Festival(self):
        self.find_element_clickable_element_by_xpath("//a[@href='/sundance/?ref_=nv_ev_sun']", wait=15).click()

    #

    def click_Toronto_Intl_Film_Festival(self):
        self.find_element_clickable_element_by_xpath("//a[@href='/toronto/?ref_=nv_ev_tor']", wait=15).click()
        time.sleep(5)

    #

    def click_Awards_central(self):
        self.find_element_clickable_element_by_xpath("//a[@href='/awards-central/?ref_=nv_ev_awrd']", wait=15).click()

    #

    def click_Festival_Central(self):
        self.find_element_clickable_element_by_xpath("//a[@href='/festival-central/?ref_=nv_ev_fc']", wait=15).click()

    #

    def click_All_Events(self):
        self.find_element_clickable_element_by_xpath("//a[@href='https://www.imdb.com/event/all/?ref_=nv_ev_all']", wait=15).click()


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
        self.find_element_clickable_element_by_xpath("//a[@href='/oscars/?ref_=nv_ev_acd']", wait=15).click()
        self.find_element_clickable_element_by_xpath("//span[normalize-space()='WINNERS']", wait=5).click()
        time.sleep(5)

    def click_year_in_winners(self):
        self.find_element_clickable_element_by_xpath("//a[normalize-space()='2020']", wait=10).click()

        time.sleep(5)
