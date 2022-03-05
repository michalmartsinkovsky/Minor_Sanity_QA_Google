from selenium.webdriver.common.by import By


class Results:

    def __init__(self, driver):
        self.driver = driver

    def first_result_txt(self):
        return self.driver.find_element(By.XPATH, "(//cite[@class='iUh30 tjvcx']/span)[1]")

    def magnify_glass_icon(self):
        return self.driver.find_element(By.XPATH, "//*[contains(@aria-label,'Google') and @type='submit']")

    def list_link_results_txt(self):
        return self.driver.find_elements(By.XPATH, "//div[@class='TbwUpd NJjxre']/cite/span[1]")

    def tool_btn(self):
        return self.driver.find_element(By.XPATH, "//div[@id='hdtb-tls']")
