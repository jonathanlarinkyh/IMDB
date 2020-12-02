
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import random
import string
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

letters = [random.choice(string.ascii_lowercase) for i in
           range(random.randint(5, 26))]
password = [random.choice(string.ascii_lowercase) for l in
            range(random.randint(5, 26))]
letters2 = [random.choice(chr(random.randint(0, 65000))) for k in
            range(random.randint(5, 26))]


class PageObject:
    def click_page_down(self):
        self.driver.find_element_by_tag_name("html").send_keys(Keys.PAGE_DOWN)

    def click_page_up(self):
        self.driver.find_element_by_tag_name("html").send_keys(Keys.PAGE_UP)

    def click_enter(self):
        self.driver.find_element_by_tag_name("html").send_keys(Keys.ENTER)

    def click_backspace(self):
        self.driver.find_element_by_tag_name("html").send_keys(Keys.BACK_SPACE)

    def find_element_click_element_by_xpath(self, selector, wait=0):
        return WebDriverWait(self.driver, wait).until(EC.element_to_be_clickable((By.XPATH, selector)))

    def find_element_click_element_by_css_selector(self, selector, wait=0):
        return WebDriverWait(self.driver, wait).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))

    def find_element_visible_element_by_xpath(self, selector, wait=0):
        return WebDriverWait(self.driver, wait).until(EC.visibility_of_element_located((By.XPATH, selector)))

    def find_element_visible_element_by_link_text(self, selector, wait=0):
        return WebDriverWait(self.driver, wait).until(EC.visibility_of_element_located((By.LINK_TEXT, selector)))

    def find_element_wait_for_element_by_xpath(self, selector, wait=0):
        return WebDriverWait(self.driver, wait).until(EC.element_t((By.XPATH, selector)))


class Menu(PageObject):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_menu(self):
        self.driver.find_element_by_xpath("//label[contains(.,'Menu')]").click()


class CelebsBornToday(PageObject):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_born_today(self):
        self.find_element_visible_element_by_link_text("Born Today", wait=5).click()

    def click_death_date(self):
        self.driver.find_element_by_xpath("//a[contains(.,'Death Date')]").click()


class CelebsMostPopular(PageObject):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_most_popular(self):
        self.driver.find_element_by_link_text("Most Popular Celebs").click()

    def click_birth_date(self):
        self.driver.find_element_by_xpath("//div[2]/a[3]").click()

    def click_clear_history(self):
        self.driver.find_element_by_css_selector("#clear_rvi")

    def click_death_date(self):
        self.driver.find_element_by_xpath("//a[contains(.,'Death Date')]")


class CelebsCelebrityNews(PageObject):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_celebrity_news(self):
        self.find_element_visible_element_by_link_text("Celebrity News", wait=10).click()

    def click_load_more(self):
        self.find_element_visible_element_by_xpath("//button[@id='news-load-more']", wait=10).click()

    def click_indie_news(self):
        self.driver.find_element_by_xpath("//a[contains(.,'See All Indie News »')]").click()


class TvshowsWhatsOnTV(PageObject):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_whats_on_tv(self):
        self.driver.find_element_by_link_text("What's on TV & Streaming").click()

    def click_see_full_gallery(self):
        self.driver.find_element_by_css_selector(".article:nth-child(29) .position_bottom").click()

    def click_grid(self):
        self.driver.find_element_by_css_selector(".ipc-icon--grid-view").click()

    def choose_twitter(self):
        self.driver.find_element_by_xpath("/html/body/div/div[2]/div[2]").send_keys(Keys.PAGE_DOWN)


class TvshowsTopRated(PageObject):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_top_rated(self):
        self.driver.find_element_by_link_text("Top Rated Shows").click()

    def click_sort_by(self):
        self.driver.find_element_by_id("lister-sort-by-options").click()

    def click_number_of_ratings(self):
        Select(self.driver.find_element_by_id("lister-sort-by-options")).select_by_visible_text("Number of Ratings")

    def click_lowest_rated(self):
        self.driver.find_element_by_link_text("Lowest Rated Movies").click()

    def click_add_to_watchlist(self):
        self.driver.find_element_by_css_selector("tr:nth-child(1) .wl-ribbon").click()


class TvshowsMostPopular(PageObject):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_most_popular(self):
        self.driver.find_element_by_link_text("Most Popular Shows").click()

    def click_doc(self):
        self.driver.find_element_by_xpath("//a[contains(text(),'Documentary')]").click()

    def click_runtime(self):
        self.driver.find_element_by_css_selector(".sorting > a:nth-child(11)").click()

    def click_next(self):
        self.driver.find_element_by_xpath("(//a[contains(text(),'Next »')])[2]").click()

    def click_compact(self):
        self.driver.find_element_by_xpath("//a[contains(text(),'Compact')]").click()

    def click_share(self):
        self.driver.find_element_by_xpath("//button[contains(.,'SHARE')]").click()

    def click_copy(self):
        self.driver.find_element_by_xpath("//input[@value='https://www.imdb.com/chart/tvmeter/']").click()

    def click_search_field(self):
        self.driver.find_element_by_id("suggestion-search").click()

    def copy_text(self):
        self.driver.find_element_by_id("suggestion-search").send_keys(Keys.CONTROL + "v")

    def click_search_button(self):
        self.driver.find_element_by_id("suggestion-search").send_keys(Keys.ENTER)


class TvshowsBrowseTvshows(PageObject):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_browse(self):
        self.driver.find_element_by_link_text("Browse TV Shows by Genre").click()

    def click_search(self):
        self.driver.find_element_by_xpath("//a[contains(text(),'Browse/Search by keyword')]").click()

    def click_searchfield(self):
        self.driver.find_element_by_xpath("//div[@id='main']/div/div/form/input[3]").send_keys("laser")

    def click_go(self):
        self.driver.find_element_by_css_selector(".btn").click()

    def click_bmovie(self):
        self.driver.find_element_by_xpath("//a[contains(text(),'B-Movie')]").click()

    def click_murder(self):
        self.driver.find_element_by_xpath("//label[12]/input")

    def choose_year(self):
        Select(self.driver.find_element_by_xpath("//select[@name='sort']")).select_by_visible_text("Year")


class TvshowsTvnews(PageObject):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_tvnews(self):
        self.driver.find_element_by_link_text("TV News").click()

    def click_second_article(self):
        self.driver.find_element_by_xpath("//section[@id='news-article-list']/article[2]/header/h2/a").click()

    def click_top_news(self):
        self.driver.find_element_by_xpath("//a[contains(.,'See All Top News »')]").click()


class TvshowsIndian(PageObject):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_indian_tv(self):
        self.driver.find_element_by_link_text("India TV Spotlight").click()

    def click_top_rated(self):
        self.driver.find_element_by_xpath("//li[3]/a/span").click()

    def click_see_more(self):
        self.driver.find_element_by_css_selector(".article:nth-child(9) .position_bottom").click()

    def click_descending(self):
        self.driver.find_element_by_xpath("//span/div/div/div[3]/div/div/div/span").click()

    def click_most_anticipated(self):
        self.driver.find_element_by_xpath("//a[contains(text(),'Most Anticipated Indian Movies and Shows')]").click()

    def click_second_on_list(self):
        self.driver.find_element_by_xpath("//span[@id='trending-list-rank-item-name-2']").click()

    def click_clear_history(self):
        self.driver.find_element_by_xpath("//a[contains(text(),'Clear your history')]").click()


class CreateUser(PageObject):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_sign_in(self):
        self.driver.find_element_by_xpath("//nav[@id='imdbHeader']/div[2]/div[5]/a/div").click()

    def click_create_account(self):
        self.driver.find_element_by_link_text("Create a New Account").click()

    def generate_name_email_ascii(self):
        maillist = ["@hotmail.com", "@gmail.com", "@yahoo.com", "@mail.com"]
        mail = [random.choice(maillist)]
        self.driver.find_element_by_xpath("//input[@id='ap_customer_name']").send_keys(letters)
        self.driver.find_element_by_xpath("//input[@id='ap_email']").send_keys(letters + mail)

    def generate_name_email_chr(self):
        maillist = ["@hotmail.com", "@gmail.com", "@yahoo.com", "@mail.com"]
        mail = [random.choice(maillist)]
        self.driver.find_element_by_xpath("//input[@id='ap_customer_name']").send_keys(letters2)
        self.driver.find_element_by_xpath("//input[@id='ap_email']").send_keys(letters2 + mail)

    def generate_password(self):
        self.driver.find_element_by_css_selector("#ap_password").send_keys(password)
        self.driver.find_element_by_css_selector("#ap_password_check").send_keys(password)
        print("".join(password))

    def create(self):
        self.driver.find_element_by_xpath("//input[@id='continue']").click()

    def click_hear_letters(self):
        self.driver.find_element_by_xpath("//a[contains(text(),'Hear the characters')]").click()

    def click_play(self):
        self.driver.find_element_by_xpath("//*[@id='cvf-page-content']/div/div/div/div[2]/div/audio").send_keys(Keys.ENTER)

    def find_signin(self):
        self.driver.find_element_by_xpath("//*[@id='cvf-page-content']/div/div")


class Youtube(PageObject):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_f4(self):
        self.driver.find_element_by_tag_name("html").send_keys(Keys.F4)
