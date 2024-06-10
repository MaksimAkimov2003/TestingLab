
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class NumIslandsPage(BasePage):
    URL = "http://localhost:5000/num_islands"

    def open(self):
        self.driver.get(self.URL)

    @property
    def grid_input(self):
        return self.driver.find_element(By.NAME, "grid")

    @property
    def submit_button(self):
        return self.driver.find_element(By.XPATH, "//button[text()='Submit']")

    @property
    def result_text(self):
        return self.driver.find_element(By.ID, "result")
