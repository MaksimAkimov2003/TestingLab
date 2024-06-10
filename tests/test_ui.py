
import unittest
from selenium import webdriver

from page_objects.home_page import HomePage
from page_objects.num_islands_page import NumIslandsPage


class TestUI(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.home_page = HomePage(self.driver)
        self.num_islands_page = NumIslandsPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_open_home_page(self):
        self.home_page.open()
        self.assertEqual("Welcome to the homepage!", self.home_page.heading.text)

    def test_num_islands_calculation(self):
        self.num_islands_page.open()
        grid_input = [[1, 1, 1, 1, 0], [1, 1, 0, 1, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]]
        self.num_islands_page.grid_input.send_keys(str(grid_input))
        self.num_islands_page.submit_button.click()
        result = self.num_islands_page.result_text.text
        self.assertEqual("Number of islands: 1", result)

    def test_invalid_grid_format(self):
        """
        Test opening the Num Islands page and submitting an invalid grid format
        """
        self.num_islands_page.open()
        grid_input = "invalid_grid_format"
        self.num_islands_page.grid_input.send_keys(grid_input)
        self.num_islands_page.submit_button.click()
        error_message = self.num_islands_page.error_message.text
        self.assertEqual("Invalid grid format", error_message)

    def test_empty_grid(self):
        """
        Test opening the Num Islands page and submitting an empty grid
        """
        self.num_islands_page.open()
        grid_input = ""
        self.num_islands_page.grid_input.send_keys(grid_input)
        self.num_islands_page.submit_button.click()
        error_message = self.num_islands_page.error_message.text
        self.assertEqual("Invalid grid format", error_message)

    def test_invalid_cell_value(self):
        """
        Test opening the Num Islands page and submitting a grid with invalid cell values
        """
        self.num_islands_page.open()
        grid_input = [[1, 1, 1], [1, "X", 1], [1, 1, 1]]
        self.num_islands_page.grid_input.send_keys(str(grid_input))
        self.num_islands_page.submit_button.click()
        error_message = self.num_islands_page.error_message.text
        self.assertEqual("Invalid cell value", error_message)

    def test_recursion_limit_exceeded(self):
        """
        Test opening the Num Islands page and submitting a grid that causes recursion limit exceeded error
        """
        self.num_islands_page.open()
        grid_input = [["1" for _ in range(1000)] for _ in range(1000)]  # Large grid to exceed recursion limit
        self.num_islands_page.grid_input.send_keys(str(grid_input))
        self.num_islands_page.submit_button.click()
        error_message = self.num_islands_page.error_message.text
        self.assertEqual("Recursion limit exceeded", error_message)

    def test_home_page_button_navigation(self):
        """
        Test navigation from Num Islands page back to the Home page
        """
        self.num_islands_page.open()
        self.num_islands_page.home_button.click()
        self.assertEqual("Welcome to the homepage!", self.home_page.heading.text)

    def test_num_islands_page_button_navigation(self):
        """
        Test navigation from Home page to the Num Islands page
        """
        self.home_page.open()
        self.home_page.num_islands_button.click()
        self.assertEqual("Number of Islands Calculation", self.num_islands_page.heading.text)

    def test_page_title(self):
        """
        Test the title of the Home page
        """
        self.home_page.open()
        self.assertEqual("Welcome to the Homepage", self.driver.title)


if __name__ == "__main__":
    unittest.main()
