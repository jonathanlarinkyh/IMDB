
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import random
import string

letters = [random.choice(chr(random.randint(0, 65000)) + string.ascii_lowercase) for i in
           range(random.randint(5, 26))]
password = [random.choice(chr(random.randint(0, 65000)) + string.ascii_lowercase) for l in
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





class Menu(PageObject):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_menu(self):
        self.driver.find_element_by_xpath("//label[contains(.,'Menu')]").click()


class CelebsBornToday(PageObject):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_born_today(self):
        self.driver.find_element_by_link_text("Born Today").click()

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
        self.driver.find_element_by_link_text("Celebrity News").click()

    def click_load_more(self):
        self.driver.find_element_by_xpath("//button[@id='news-load-more']").click()

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


class CreateUser(PageObject):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_sign_in(self):
        self.driver.find_element_by_xpath("//nav[@id='imdbHeader']/div[2]/div[5]/a/div").click()


    def click_create_account(self):
        self.driver.find_element_by_link_text("Create a New Account").click()


    def generate_name_email(self):
        #letters = [random.choice(chr(random.randint(0, 65000)) + string.ascii_lowercase) for i in
                   #range(random.randint(5, 26))]

        maillist = ["@hotmail.com", "@gmail.com", "@yahoo.com", "@mail.com"]
        mail = [random.choice(maillist)]
        self.driver.find_element_by_xpath("//input[@id='ap_customer_name']").send_keys(letters)
        self.driver.find_element_by_xpath("//input[@id='ap_email']").send_keys(letters + mail)


    def generate_password(self):
        #password = [random.choice(chr(random.randint(0, 65000))) for i in
                    #range(random.randint(5, 26))]
        self.driver.find_element_by_css_selector("#ap_password").send_keys(password)
        self.driver.find_element_by_css_selector("#ap_password_check").send_keys(password)
        print("".join(password))

    def create(self):
        self.driver.find_element_by_xpath("//input[@id='continue']").click()



    def click_hear_letters(self):
        self.driver.find_element_by_xpath("//a[contains(text(),'Hear the characters')]").click()




