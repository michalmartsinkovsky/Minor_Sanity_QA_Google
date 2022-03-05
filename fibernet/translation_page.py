from selenium.webdriver.common.by import By


class Translation:

    def __init__(self, driver):
        self.driver = driver

    def text_area(self):
        return self.driver.find_element(By.XPATH, "//div[@class='OPPzxe']/c-wiz[1]/span/span/div/textarea")

    def result_table(self):
        return self.driver.find_element(By.XPATH, "//div[@class='Dwvecf']/table")


