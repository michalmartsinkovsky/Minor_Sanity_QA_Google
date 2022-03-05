import csv
from webdriver_manager.firefox import GeckoDriverManager
import pytest
from smart_assertions import soft_assert, verify_expectations
from translation_page import Translation
from web_flow import Web_Flow
from google_apps import Google_apps
from search_input import SearchInput
from search_results import Results
from header import HeaderMenu
from selenium import webdriver

browser_type = "chrome"


def read_file_csv(name_file):
    users_list_from_csv_file = []
    file1 = open(name_file, "r", encoding='UTF8')
    reading = csv.reader(file1)
    for row in reading:
        users_list_from_csv_file.append(row)
    file1.close()
    return tuple(users_list_from_csv_file)


class Test_sanity:

    def setup_class(cls):
        global driver
        global header_menu
        global search_page
        global results_page
        global apps
        global translate

        if browser_type.lower() == "chrome":
            driver = webdriver.Chrome('chromedriver.exe')
        elif browser_type == "firefox":
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif browser_type == "edge":
            driver = webdriver.Edge('msedgedriver.exe')
        else:
            raise Exception("Wrong browser type")

        driver.maximize_window()
        driver.get("https://www.google.com/")

        # page objects initiation
        header_menu = HeaderMenu(driver)
        search_page = SearchInput(driver)
        results_page = Results(driver)
        apps = Google_apps(driver)

        translate = Translation(driver)

    def teardown_class(cls):
        driver.quit()

    file_csv = read_file_csv("search_input_and_expected_result.csv")

    @pytest.mark.parametrize("search, result", file_csv)
    def test_searching_text_using_csv_file(self, search, result):
        Web_Flow.searching_text_from_csv_file(search_page, search)
        results = results_page.list_link_results_txt()
        soft_assert(results[0].text == result)
    verify_expectations()

    def test_searching_text(self):
        Web_Flow.searching_text_using_down_arrows(search_page, "angelina jolie")
        results = results_page.list_link_results_txt()
        expected = "https://en.wikipedia.org"
        assert (results[0].text, expected)

    def test_google_apps(self):
        Web_Flow.click_google_apps(header_menu)
        Web_Flow.change_to_apps_iframe(driver, apps, "Translate")
        expected = "https://translate.google.co.il/?hl=iw&tab=wT"
        soft_assert(driver.current_url, expected)
        translation_success = Web_Flow.translating(translate, "הצלחה")
        soft_assert(translation_success, True)
    verify_expectations()

    def test_change_web_language_interface(self):
        driver.get("https://www.google.com/")
        is_english = Web_Flow.change_language(driver, search_page)
        if is_english:
            expected = "Israel"
        else:
            expected = "ישראל"
        assert (search_page.footer_country_name().text, expected)
