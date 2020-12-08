import unittest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import imdb_page

options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')
print(help(EC.presence_of_all_elements_located))

WEBDRIVER = "CHROME"


def webdriver_chrome():
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.back()
    driver.forward()
    return driver


def webdriver_chrome_headless():
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 1080)
    driver.implicitly_wait(10)
    driver.back()
    driver.forward()
    return driver


def webdriver_factory():
    if WEBDRIVER == "CHROME":
        return webdriver_chrome()
    elif WEBDRIVER == "CHROME_HEADLESS":
        return webdriver_chrome_headless()
    else:
        return webdriver_chrome()


class IMDB_Home_Page_test(unittest.TestCase):

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)

    def setUp(self):
        self.driver = webdriver_chrome()
        self.driver.get("https://www.imdb.com/?ref_=nv_home")

    def tearDown(self):
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        name = 'screenshot-%s.png' % now
        self.driver.get_screenshot_as_file(name)
        print("Tearing Down Awards & Events_Section: Nav Test")
        self.driver.quit()

    def foo_test_home_page(self):
        main_page = imdb_page.IMDBMainPage(self.driver)
        main_page.page_down()
        main_page.page_whole_down()
        main_page.page_whole_up()
        main_page.click_browse_trailers()
        main_page.page_whole_down()
        main_page.page_whole_up()
        main_page.click_back_page()

    def test_home_top_picks(self):
        main_page = imdb_page.IMDBMainPage(self.driver)
        main_page.page_down()
        main_page.click_fan_favorite()
        main_page.page_whole_down()
        main_page.page_whole_up()
        main_page.click_top_picks()
        main_page.page_down()
        main_page.page_down()
        main_page.click_back_page()
        main_page.click_back_page()


class test_IMBD_Nav(unittest.TestCase):
    base_url = "https://www.imdb.com"

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.target_url = "https://www.imdb.com"

    def setUp(self):
        self.driver = webdriver_chrome()
        self.driver.get("https://www.imdb.com")

    def test_page_access(self):
        main_page = self.driver.get("https://imdb.com")

    def tearDown(self):
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        name = 'screenshot-%s.png' % now
        self.driver.get_screenshot_as_file(name)
        print("Tearing Down Awards & Events_Section: Nav Test")
        self.driver.quit()


class test_imdb_menu(unittest.TestCase):

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)

    def setUp(self):
        self.driver = webdriver_chrome()
        self.driver.get("https://www.imdb.com")

    def tearDown(self):
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        name = 'screenshot-%s.png' % now
        self.driver.get_screenshot_as_file(name)
        print("Tearing Down Awards & Events_Menu Elements")
        self.driver.quit()

    def test_click_menu(self):
        main_page = imdb_page.Menu(self.driver)
        main_page.click_menu_dd()

    def test_001_menu_oscars(self):
        main_page = imdb_page.IMDB_menu_awards_and_events(self.driver)
        main_page.click_menu_dd()
        main_page.click_oscars()
        main_page.page_whole_down()

    def test_002_menu_BPW(self):
        main_page = imdb_page.IMDB_menu_awards_and_events(self.driver)
        main_page.click_menu_dd()
        main_page.click_best_picture_Winner()
        main_page.page_down()

    def test_003_menu_Golden_Globes(self):
        main_page = imdb_page.IMDB_menu_awards_and_events(self.driver)
        main_page.click_menu_dd()
        main_page.click_Golden_Globes()
        main_page.page_whole_down()

    def test_004_menu_Emmys(self):
        main_page = imdb_page.IMDB_menu_awards_and_events(self.driver)
        main_page.click_menu_dd()
        main_page.click_Emmys()
        self.assertEqual(self.driver.find_element_by_xpath("//h1[normalize-space()='EMMYS']").text,
                         "EMMYS", msg="Not Emmys")

    def test_005_menu_STARmeter_Awards(self):
        main_page = imdb_page.IMDB_menu_awards_and_events(self.driver)
        main_page.click_menu_dd()
        main_page.click_STARmeter_Awards()
        self.assertEqual(self.driver.find_element_by_xpath("//h1[normalize-space()='IMDb STARmeter AWARDS']").text,
                         "IMDb STARmeter AWARDS", msg="Wrong Page Not STARmeter Awards")

    def test_006_menu_SD_Comic_Con(self):
        main_page = imdb_page.IMDB_menu_awards_and_events(self.driver)
        main_page.click_menu_dd()
        main_page.click_SanDiego_Comic_Con()
        self.assertEqual(self.driver.find_element_by_xpath("//*[@id='widget-nav']/div[1]/div/a/h1").text,
                         "SAN DIEGO COMIC-CON", msg="Wrong Page Not SD COMIC CON")

    def test_007_menu_NY_Comic_Con(self):
        main_page = imdb_page.IMDB_menu_awards_and_events(self.driver)
        main_page.click_menu_dd()
        main_page.click_NY_Comic_Con()
        self.assertEqual(self.driver.find_element_by_xpath("//h1[normalize-space()='NEW YORK COMIC CON']").text,
                         "NEW YORK COMIC CON", msg="Wrong Page Not NY COMIC CON")

    def test_008_menu_Sundance_FF(self):
        main_page = imdb_page.IMDB_menu_awards_and_events(self.driver)
        main_page.click_menu_dd()
        main_page.click_Sundance_Film_Festival()
        self.assertEqual(self.driver.find_element_by_xpath("//h1[normalize-space()='SUNDANCE FILM FESTIVAL']").text,
                         "SUNDANCE FILM FESTIVAL", msg="Wrong Page Not SUNDANCE FILM FESTIVAL")

    def test_009_menu_Toronto_Intl_FF(self):
        main_page = imdb_page.IMDB_menu_awards_and_events(self.driver)
        main_page.click_menu_dd()
        main_page.click_Toronto_Intl_Film_Festival()
        self.assertEqual(self.driver.find_element_by_xpath("//h1[normalize-space()='TORONTO INTERNATIONAL FILM FESTIVAL']").text,
                         "TORONTO INTERNATIONAL FILM FESTIVAL", msg="Wrong Page Not TORONTO INTL FILM FESTIVAL")

    def test_009_menu_AWARD_CENTRAL(self):
        main_page = imdb_page.IMDB_menu_awards_and_events(self.driver)
        main_page.click_menu_dd()
        main_page.click_Awards_central()
        self.assertEqual(
            self.driver.find_element_by_xpath("//h1[normalize-space()='AWARDS CENTRAL']").text,
            "AWARDS CENTRAL", msg="Wrong Page Not AWARD CENTRAL")

    def test_010_menu_Festival_Central(self):
        main_page = imdb_page.IMDB_menu_awards_and_events(self.driver)
        main_page.click_menu_dd()
        main_page.click_Festival_Central()
        self.assertEqual(
            self.driver.find_element_by_xpath("//h1[normalize-space()='FESTIVAL CENTRAL']").text,
            "FESTIVAL CENTRAL", msg="Wrong Page Not FESTIVAL CENTRAL")

    def test_011_menu_All_Events(self):
        main_page = imdb_page.IMDB_menu_awards_and_events(self.driver)
        main_page.click_menu_dd()
        main_page.click_All_Events()
        self.assertEqual(
            self.driver.find_element_by_xpath("//h1[normalize-space()='All Events']").text,
            "All Events", msg="Wrong Page Not All Events")


class test_Awards_and_Events_Oscars(unittest.TestCase):

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)

    def setUp(self):
        self.driver = webdriver_chrome()
        self.driver.get("https://www.imdb.com")

    def tearDown(self):
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        name = 'screenshot-%s.png' % now
        self.driver.get_screenshot_as_file(name)
        print("Tearing Down Awards & Events_Section: Oscar")
        self.driver.quit()

    def test_elements_of_oscars(self):
        main_page = imdb_page.IMDB_Menu_Oscars(self.driver)
        main_page.click_oscars_menu()
        main_page.click_oscars_main()

    def test_winners_in_oscars(self):
        main_page = imdb_page.IMDB_Menu_Oscars(self.driver)
        main_page.click_oscars_menu()
        main_page.click_winners_in_oscar()
        main_page.page_down()
        main_page.page_down()

    def test_year_in_winners(self):
        main_page = imdb_page.IMDB_Menu_Oscars(self.driver)
        main_page.click_oscars_menu()
        main_page.click_winners_in_oscar()
        main_page.click_year_in_winners()


class IMDB_User_login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver_chrome()
        self.driver.get("https://www.imdb.com/?ref_=nv_home")

    def tearDown(self):
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        name = 'Reports/screenshot-%s.png' % now
        self.driver.get_screenshot_as_file(name)
        print("User Login Tearing Down")
        self.driver.quit()

    def test_create_user_ascii(self):
        main_page = imdb_page.CreateUser(self.driver)
        main_page.click_sign_in()
        main_page.click_create_account()
        main_page.generate_name_email_ascii()
        main_page.generate_password()
        main_page.create()
        main_page.click_hear_letters()
        main_page.click_play()
        self.assertEqual(self.driver.current_url, "https://www.imdb.com/ap/cvf/verify")

    def test_create_user_chr(self):
        main_page = imdb_page.CreateUser(self.driver)
        main_page.click_sign_in()
        main_page.click_create_account()
        main_page.generate_name_email_chr()
        main_page.generate_password()
        main_page.create()
