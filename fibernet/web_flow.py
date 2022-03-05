import time
import allure
from selenium.webdriver import Keys


class Web_Flow:
    tool_tab = ""

    @staticmethod
    @allure.step("searching words from csv file")
    def searching_text_from_csv_file(page, search):
        page.search_input().send_keys(search)
        page.search_input().send_keys(Keys.RETURN)
        page.search_input().click()
        page.search_input().send_keys(Keys.CONTROL, "a")
        page.search_input().send_keys(Keys.DELETE)
        time.sleep(1)

    @staticmethod
    @allure.step("searching word using down arrow")
    def searching_text_using_down_arrows(page, search):

        page.search_input().send_keys(search)
        time.sleep(1)
        page.search_input().send_keys(Keys.DOWN)
        page.search_input().send_keys(Keys.DOWN)
        page.search_input().send_keys(Keys.DOWN)
        page.search_input().send_keys(Keys.RETURN)
        time.sleep(1)

    @staticmethod
    @allure.step("click on the apps icon")
    def click_google_apps(page):
        page.google_apps_btn().click()

    @staticmethod
    @allure.step("choosing the translation app")
    def change_to_apps_iframe(driver, page, app_name):

        frame = page.iframe()
        driver.switch_to.frame(frame)
        list_apps = page.list_of_apps_btn()

        for app in list_apps:
            if app.text == app_name:
                app.click()
                break
        time.sleep(2)

    @staticmethod
    @allure.step("using the translation app")
    def translating(page, word):
        page.text_area().send_keys(word)
        time.sleep(2)
        return page.result_table().is_displayed()

    @staticmethod
    @allure.step("change the default language to either hebrew or english")
    def change_language(driver, page):

        page_type = type(page)
        page_name = page_type.__name__
        if page_name == "HeaderMenu":
            is_english = False
            if not Web_Flow.tool_tab == 'Tools':
                is_english = True
                page.choose_english_language_from_setting_btn().click()
            else:
                page.choose_hebrew_language_from_setting_btn().click()

            page.save_btn_from_setting().click()
            popup = driver.switch_to.alert
            popup.accept()
        else:
            Web_Flow.tool_tab = page.footer_country_name().text
            if not Web_Flow.tool_tab == 'Israel':
                is_english = True
                page.change_to_english_btn().click()
            else:
                page.change_to_arabic_btn().click()
        return is_english
