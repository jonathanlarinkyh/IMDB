import random
import string
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

# User Generator
letters = [random.choice(string.ascii_lowercase) for i in
           range(random.randint(5, 26))]
password = [random.choice(string.ascii_lowercase) for p in
            range(random.randint(5, 26))]
letters2 = [random.choice(chr(random.randint(0, 65000))) for k in
            range(random.randint(5, 26))]


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

    def page_whole_down(self):
        for page in range(0, 8):
            self.driver.find_element_by_tag_name("html").send_keys(Keys.PAGE_DOWN)

    def click_back_page(self):
        self.driver.back()

    def click_forward_page(self):
        self.driver.forward()

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

    def click_menu_dd(self):
        self.find_element_clickable_element_by_xpath("//label[contains(.,'Menu')]", wait=10).click()

    def click_browse_trailers(self):
        self.find_element_clickable_element_by_xpath("//a[normalize-space()='Browse trailers']", wait=10).click()

    def click_top_picks(self):
        self.find_element_clickable_element_by_xpath("//*[@id='__next']/main/div[2]/section/section/section/div[1]/ul/li[3]/span", wait=20).click()

    def click_fan_favorite(self):
        self.find_element_clickable_element_by_xpath("//h3[normalize-space()='Fan favorites']", wait=10).click()


class Menu(PageObject):

    def __init__(self, driver: webdriver.Chrome):
        super().__init__()
        self.driver = driver

    def click_menu_dd(self):
        self.find_element_clickable_element_by_xpath("//label[contains(.,'Menu')]", wait=10).click()


class IMDBMenuMovies(PageObject):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__()
        self.driver = driver

    def click_home(self):
        self.driver.find_element_by_xpath("(//a[contains(@href, '/?ref_=nv_home')])[2]").click()

    def click_menu_dd(self):
        self.find_element_clickable_element_by_xpath("//label[contains(.,'Menu')]", wait=10).click()

    def click_menu_dd_release_calendar(self):
        self.find_element_clickable_element_by_xpath("//a[contains(@href, 'https://www.imdb.com/calendar/?ref_=nv_mv_cal')]", wait=10).click()

    def click_menu_dd_dvd_blue_releases(self):
        self.find_element_clickable_element_by_xpath("//a[contains(@href, 'https://www.imdb.com/list/ls016522954/?ref_=nv_tvv_dvd')]", wait=10).click()

    def click_menu_dd_top_rated_movies(self):
        self.find_element_clickable_element_by_xpath("//a[contains(@href, '/chart/top/?ref_=nv_mv_250')]", wait=10).click()

    def click_menu_dd_most_popular_movies(self):
        self.find_element_clickable_element_by_xpath("//a[contains(@href, '/chart/moviemeter/?ref_=nv_mv_mpm')]", wait=10).click()

    def click_menu_dd_browse_movies_by_genre(self):
        self.find_element_clickable_element_by_xpath("//a[contains(@href, 'https://www.imdb.com/feature/genre/?ref_=nv_ch_gr')]", wait=10).click()

    def click_menu_dd_top_box_office(self):
        self.find_element_clickable_element_by_xpath("//a[contains(@href, '/chart/boxoffice/?ref_=nv_ch_cht')]", wait=10).click()

    def click_menu_dd_showtime_tickets(self):
        self.find_element_clickable_element_by_xpath("//a[contains(@href, 'https://www.imdb.com/showtimes/?ref_=nv_mv_sh')]", wait=10).click()

    def click_menu_dd_in_theater(self):
        self.find_element_clickable_element_by_xpath("//a[contains(@href, 'https://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth')]", wait=10).click()

    def click_menu_dd_coming_soon(self):
        self.find_element_clickable_element_by_xpath("//a[contains(@href, 'https://www.imdb.com/coming-soon/?ref_=nv_mv_cs')]", wait=10).click()

    def click_menu_dd_movie_news(self):
        self.find_element_clickable_element_by_xpath("//a[contains(.,'Movie News')]", wait=10).click()

    def click_menu_dd_india_movie_spotlight(self):
        self.find_element_clickable_element_by_xpath("//a[contains(.,'India Movie Spotlight')]", wait=10).click()


class ReleaseCalendar(PageObject):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__()
        self.driver = driver

    def click_clear_history(self):
        self.find_element_clickable_element_by_css_selector("#clear_rvi", wait=10).click()

    def click_first_choice(self):
        self.find_element_clickable_element_by_css_selector("#main > ul:nth-child(2) a", wait=10).click()

    def click_second_choice(self):
        self.find_element_clickable_element_by_css_selector("ul:nth-child(4) > li:nth-child(1) > a", wait=10).click()

    def click_director(self):
        self.find_element_clickable_element_by_css_selector(".credit_summary_item:nth-child(2) > a", wait=10).click()

    def history_clickable_first_image(self):
        self.find_element_clickable_element_by_xpath("//div[3]/div/div[2]/div/a/img", wait=10).click()


class DVDnBlue(PageObject):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__()
        self.driver = driver

    def click_first_choice(self):
        self.find_element_clickable_element_by_css_selector(".lister-item:nth-child(1) .loadlate", wait=10).click()


class CelebsBornToday(PageObject):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__()
        self.driver = driver

    def click_born_today(self):
        self.find_element_visible_element_by_link_text("Born Today", wait=5).click()

    def click_death_date(self):
        self.driver.find_element_by_xpath("//a[contains(.,'Death Date')]").click()


class CelebsMostPopular(PageObject):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__()
        self.driver = driver

    def click_most_popular(self):
        self.driver.find_element_by_link_text("Most Popular Celebs").click()

    def click_birth_date(self):
        self.find_element_clickable_element_by_xpath("//div[2]/a[3]", wait=5).click()

    def click_clear_history(self):
        self.driver.find_element_by_css_selector("#clear_rvi")

    def click_death_date(self):
        self.driver.find_element_by_xpath("//a[contains(.,'Death Date')]")


class CelebsCelebrityNews(PageObject):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__()
        self.driver = driver

    def click_celebrity_news(self):
        self.find_element_visible_element_by_link_text("Celebrity News", wait=10).click()

    def click_load_more(self):
        self.find_element_clickable_element_by_xpath("//button[@id='news-load-more']", wait=10).click()

    def click_indie_news(self):
        self.find_element_clickable_element_by_xpath("//a[contains(.,'See All Indie News »')]").click()


class TvshowsWhatsOnTV(PageObject):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__()
        self.driver = driver

    def click_whats_on_tv(self):
        self.driver.find_element_by_link_text("What's on TV & Streaming").click()

    def click_see_full_gallery(self):
        self.driver.find_element_by_css_selector(".article:nth-child(29) .position_bottom").click()

    def click_grid(self):
        self.driver.find_element_by_css_selector(".ipc-icon--grid-view").click()

    def click_holiday(self):
        self.driver.find_element_by_link_text("See the full gallery")


class TvshowsTopRated(PageObject):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__()
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
        super().__init__()
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
        super().__init__()
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
        super().__init__()
        self.driver = driver

    def click_tvnews(self):
        self.driver.find_element_by_link_text("TV News").click()

    def click_second_article(self):
        self.driver.find_element_by_xpath("//section[@id='news-article-list']/article[2]/header/h2/a").click()

    def click_top_news(self):
        self.driver.find_element_by_xpath("//a[contains(.,'See All Top News »')]").click()


class TvshowsIndian(PageObject):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__()
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
        super().__init__()
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

    def change_otp_method(self):
        self.find_element_clickable_element_by_xpath("//a[normalize-space()='(Change)']", wait=10).click()


class IMDBMenuWatch(PageObject):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__()
        self.driver = driver

    def click_home(self):
        self.driver.find_element_by_xpath("(//a[contains(@href, '/?ref_=nv_home')])[2]").click()

    def click_dd_menu(self):
        self.find_element_clickable_element_by_xpath("//label[@id='imdbHeader-navDrawerOpen--desktop']", wait=10).click()

    def click_dd_menu_whats_new(self):
        self.find_element_clickable_element_by_xpath("//a[contains(@href, '/what-to-watch/?ref_=nv_watch')]", wait=10).click()

    def click_dd_menu_latest_trailers(self):
        self.find_element_clickable_element_by_xpath("//a[contains(@href, '/trailers/?ref_=nv_mv_tr')]", wait=10).click()

    def click_dd_menu_originals(self):
        self.find_element_clickable_element_by_xpath("//a[contains(@href, '/originals/?ref_=nv_sf_ori')]", wait=10).click()

    def click_dd_menu_picks(self):
        self.find_element_clickable_element_by_xpath("//a[contains(@href, '/imdbpicks/?ref_=nv_pi')]", wait=10).click()

    def click_dd_menu_podcasts(self):
        self.find_element_clickable_element_by_xpath("//a[contains(@href, '/podcasts/?ref_=nv_pod')]", wait=10).click()


class IMDBWhatToWatch(PageObject):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__()
        self.driver = driver

    def click_most_popular(self):
        self.find_element_clickable_element_by_xpath("//li[5]/span", wait=10).click()

    def click_fan_favorites(self):
        self.find_element_clickable_element_by_css_selector(".ipc-tab:nth-child(2) > span", wait=10).click()

    def click_first_choice(self):
        self.find_element_clickable_element_by_xpath("//a/div[2]", wait=10).click()

    def pick_first_movie(self):
        self.find_element_clickable_element_by_xpath("//h3/a", wait=10).click()

    def check_history(self):
        self.find_element_clickable_element_by_css_selector("recently-viewed > .header", wait=10)

    def click_clear_history(self):
        self.find_element_clickable_element_by_css_selector("#clear_rvi", wait=10).click()


class IMDB_menu_awards_and_events(PageObject):

    def __init__(self, driver: webdriver.Chrome):
        super().__init__()
        self.driver = driver

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
