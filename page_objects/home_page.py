
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class HomePage(BasePage):
    URL = "http://localhost:5000/"

    def open(self):
        self.driver.get(self.URL)

    @property
    def heading(self):
        return self.driver.find_element(By.TAG_NAME, "h1")
