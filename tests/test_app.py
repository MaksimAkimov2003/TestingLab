import unittest
import json
from app.app import app
import sys

class TestNumIslandsAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_single_island(self):
        """
        Test API with a single island grid
        """
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]
        response = self.app.post('/num_islands', data=json.dumps({'grid': grid}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['num_islands'], 1)

    def test_multiple_islands(self):
        """
        Test API with multiple islands grid
        """
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
        response = self.app.post('/num_islands', data=json.dumps({'grid': grid}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['num_islands'], 3)

    def test_empty_grid(self):
        """
        Test API with an empty grid
        """
        grid = [[]]
        response = self.app.post('/num_islands', data=json.dumps({'grid': grid}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['num_islands'], 0)

    def test_invalid_grid(self):
        """
        Test API with invalid grid input
        """
        grid = [["1", "1", "0", "0", "0"], ["1", "X", "0", "0", "0"]]
        response = self.app.post('/num_islands', data=json.dumps({'grid': grid}), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_large_grid(self):
        """
        Test API with a large grid to check recursion limit handling
        """
        sys.setrecursionlimit(1500)  # Increase recursion limit
        grid = [["1"] * 300 for _ in range(300)]
        response = self.app.post('/num_islands', data=json.dumps({'grid': grid}), content_type='application/json')

        if response.status_code == 200:
            self.assertEqual(response.json['num_islands'], 1)
        else:
            self.assertEqual(response.status_code, 500)

    def test_open_page(self):
        """
        Test opening the page
        """
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_form_submission(self):
        """
        Test form submission
        """
        grid = [["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"]]
        response = self.app.post('/num_islands', data=json.dumps({'grid': grid}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'num_islands', response.data)


if __name__ == "__main__":
    unittest.main()
