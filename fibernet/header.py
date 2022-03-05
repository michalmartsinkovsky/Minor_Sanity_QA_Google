from selenium.webdriver.common.by import By


class HeaderMenu:

    def __init__(self, driver):
        self.driver = driver

    def gmail_btn(self):
        return self.driver.find_element(By.XPATH, "//div[@class='gb_e gb_f']/a[@data-pid='23']")

    def images_btn(self):
        return self.driver.find_element(By.XPATH, "//div[@class='gb_e gb_f']/a[@data-pid='2']")

    def google_apps_btn(self):
        return self.driver.find_element(By.XPATH, "//div[@class='gb_wf']")

    def google_account_btn(self):
        return self.driver.find_element(By.XPATH, "//div[@class='gb_wf gb_Ua gb_jg gb_f']/a[@class='gb_A gb_Ka gb_f']")

    def setting_btn(self):
        return self.driver.find_element(By.XPATH, "//div[@class='c58wS']/div")

    def choose_language_from_setting_btn(self):
        return self.driver.find_element(By.XPATH, "//div[@class='q0yked']/a[contains(@href, 'languages')]")

    def choose_english_language_from_setting_btn(self):
        return self.driver.find_element(By.XPATH, "//div[@id='langtop']/div/div[2]")

    def choose_hebrew_language_from_setting_btn(self):
        return self.driver.find_element(By.XPATH, "//div[@id='langoiw']/div/span")

    def save_btn_from_setting(self):
        return self.driver.find_element(By.XPATH, "//div[@id='form-buttons']/div[1]")

    def tool_btn(self):
        return self.driver.find_element(By.XPATH, "//div[@id='hdtb-tls']")


