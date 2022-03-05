from selenium.webdriver.common.by import By


class Google_apps:

    def __init__(self, driver):
        self.driver = driver

    def iframe(self):
        return self.driver.find_element(By.XPATH, "(//iframe[@role='presentation'])[1]")

    def list_of_apps_btn(self):
        return self.driver.find_elements(By.XPATH, "//ul[@class='LVal7b u4RcUd']/li")

    def translate_btn(self):
        return self.driver.find_element(By.XPATH,
                                        "//ul[@class='LVal7b u4RcUd']/li/a[@href='https://translate.google.co.il/?hl=iw']")
