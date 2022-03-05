from selenium.webdriver.common.by import By


class SearchInput:

    def __init__(self, driver):
        self.driver = driver

    def search_input(self):
        return self.driver.find_element(By.XPATH, "//input[@name='q']")

    def list_input(self):
        return self.driver.find_element(By.XPATH, "//ul[@class='G43f7e']/li")

    def magnify_glass_icon(self):
        return self.driver.find_element(By.XPATH, "//*[contains(@aria-label,'Google') and @type='submit']")

    def search_by_voice_btn(self):
        return self.driver.find_element(By.XPATH, "//div[@aria-label='Search by voice']")

    def google_search_btn(self):
        return self.driver.find_element(By.XPATH, "//div[@class='FPdoLc lJ9FBc']/center/input[@class='gNO89b']")

    def i_feel_lucky_btn(self):
        return self.driver.find_element(By.XPATH, "//div[@class='FPdoLc lJ9FBc']/center/input[@class='RNmpXc']")

    def change_to_english_btn(self):
        return self.driver.find_element(By.XPATH, "//div[@id='SIvCob']/a[2]")

    def change_to_arabic_btn(self):
        return self.driver.find_element(By.XPATH, "//div[@id='SIvCob']/a[1]")

    def footer_country_name(self):
        return self.driver.find_element(By.XPATH, "//div[@class='uU7dJb']")


