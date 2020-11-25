
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select


class PageObject:
    def click_page_down(self):
        self.driver.find_element_by_tag_name("html").send_keys(Keys.PAGE_DOWN)

    def click_page_up(self):
        self.driver.find_element_by_tag_name("html").send_keys(Keys.PAGE_UP)

    def click_enter(self):
        self.driver.find_element_by_tag_name("html").send_keys(Keys.ENTER)

    def click_backspace(self):
        self.driver.find_element_by_tag_name("html").send_keys(Keys.BACK_SPACE)


class FindElementByXpath:
    def click_xpath(self):
        self.driver.find_element_by_xpath("").click()



class Menu(PageObject, FindElementByXpath):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_menu(self):
        self.driver.find_element_by_xpath("//label[contains(.,'Menu')]").click()


class CelebsBornToday(PageObject, FindElementByXpath):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_born_today(self):
        self.driver.find_element_by_xpath("//a[contains(.,'Born Today')]").click()


class CelebsMostPopular(PageObject):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_most_popular(self):
        self.driver.find_element_by_link_text("Most Popular Celebs").click()

    def click_birth_date(self):
        self.driver.find_element_by_xpath("//div[2]/a[3]").click()

    def click_clear_history(self):
        self.driver.find_element_by_css_selector("#clear_rvi")


class CelebsCelebrityNews(PageObject):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_celebrity_news(self):
        self.driver.find_element_by_xpath("//a[contains(.,'Celebrity News')]").click()

    def click_load_more(self):
        self.driver.find_element_by_xpath("//button[@id='news-load-more']").click()


class TvshowsWhatsOnTV(PageObject):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_whats_on_tv(self):
        self.driver.find_element_by_link_text("What's on TV & Streaming").click()

    def click_see_full_gallery(self):
        self.driver.find_element_by_css_selector(".article:nth-child(27) .position_bottom").click()

    def click_grid(self):
        self.driver.find_element_by_css_selector(".ipc-icon--grid-view").click()


class TvshowsTopRated(PageObject):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_top_rated(self):
        self.driver.find_element_by_link_text("Top Rated Shows").click()

    def click_sort_by(self):
        self.driver.find_element_by_id("lister-sort-by-options").click()

    def click_number_of_ratings(self):
        Select(self.driver.find_element_by_id("lister-sort-by-options")).select_by_visible_text("Number of Ratings")
        #select.select_by_visible_text("Number of Ratings")

    def click_learn_more(self):
        self.driver.find_element_by_xpath("//span/div/div/a").click()


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

class TvshowsTvnews(PageObject):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_tvnews(self):
        self.driver.find_element_by_link_text("TV News").click()

    def click_second_article(self):
        self.driver.find_element_by_xpath("//section[@id='news-article-list']/article[2]/header/h2/a").click()


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