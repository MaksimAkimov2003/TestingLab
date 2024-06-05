import unittest

from Solution import Solution


class _TestSuite(unittest.TestCase):
    def setUp(self) -> None:
        self.SUT = Solution().numIslands


class TestSolution(_TestSuite):
    def test_single_island(self):
        """
        Example 1:
        Input: grid = [
          ["1","1","1","1","0"],
          ["1","1","0","1","0"],
          ["1","1","0","0","0"],
          ["0","0","0","0","0"]
        ]
        Output: 1
        """
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]
        expected = 1
        self.assertEqual(expected, self.SUT(grid))

    def test_multiple_islands(self):
        """
        Example 2:
        Input: grid = [
          ["1","1","0","0","0"],
          ["1","1","0","0","0"],
          ["0","0","1","0","0"],
          ["0","0","0","1","1"]
        ]
        Output: 3
        """
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
        expected = 3
        self.assertEqual(expected, self.SUT(grid))

    def test_solution_single_land(self):
        """
        Test case with a single land cell.
        Input: grid = [["1"]]
        Output: 1
        """
        grid = [["1"]]
        expected = 1
        self.assertEqual(expected, self.SUT(grid))

    def test_solution_single_water(self):
        """
        Test case with a single water cell.
        Input: grid = [["0"]]
        Output: 0
        """
        grid = [["0"]]
        expected = 0
        self.assertEqual(expected, self.SUT(grid))

    def test_solution_empty_grid(self):
        """
        Test case with an empty grid.
        Input: grid = [[]]
        Output: 0
        """
        grid = [[]]
        expected = 0
        self.assertEqual(expected, self.SUT(grid))

    def test_solution_all_land(self):
        """
        Test case with a grid filled with land.
        Input: grid = [["1", "1"], ["1", "1"]]
        Output: 1
        """
        grid = [["1", "1"], ["1", "1"]]
        expected = 1
        self.assertEqual(expected, self.SUT(grid))

    def test_solution_all_water(self):
        """
        Test case with a grid filled with water.
        Input: grid = [["0", "0"], ["0", "0"]]
        Output: 0
        """
        grid = [["0", "0"], ["0", "0"]]
        expected = 0
        self.assertEqual(expected, self.SUT(grid))


class TestGridSizeValidation(_TestSuite):
    """
    Constraints:

    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.
    """

    def test_max_size_grid(self):
        """
        Test case with the maximum grid size.
        Input: grid = [["1"]*300]*300
        Output: 1
        """
        grid = [["1"] * 300] * 300
        expected = 1
        self.assertEqual(expected, self.SUT(grid))

    def test_max_size_grid_all_water(self):
        """
        Test case with the maximum grid size filled with water.
        Input: grid = [["0"]*300]*300
        Output: 0
        """
        grid = [["0"] * 300] * 300
        expected = 0
        self.assertEqual(expected, self.SUT(grid))


class TestEdgeCases(_TestSuite):
    """
    Additional edge cases for more thorough testing.
    """

    def test_one_row_land(self):
        """
        Test case with a single row filled with land.
        Input: grid = [["1", "1", "1", "1", "1"]]
        Output: 1
        """
        grid = [["1", "1", "1", "1", "1"]]
        expected = 1
        self.assertEqual(expected, self.SUT(grid))

    def test_one_row_water(self):
        """
        Test case with a single row filled with water.
        Input: grid = [["0", "0", "0", "0", "0"]]
        Output: 0
        """
        grid = [["0", "0", "0", "0", "0"]]
        expected = 0
        self.assertEqual(expected, self.SUT(grid))

    def test_horizontal_islands(self):
        """
        Test case with horizontal islands.
        Input: grid = [["1","0","1"], ["1","0","1"], ["1","0","1"]]
        Output: 2
        """
        grid = [["1", "0", "1"], ["1", "0", "1"], ["1", "0", "1"]]
        expected = 2
        self.assertEqual(expected, self.SUT(grid))

    def test_vertical_islands(self):
        """
        Test case with vertical islands.
        Input: grid = [["1","1","1"], ["0","0","0"], ["1","1","1"]]
        Output: 2
        """
        grid = [["1", "1", "1"], ["0", "0", "0"], ["1", "1", "1"]]
        expected = 2
        self.assertEqual(expected, self.SUT(grid))

    def test_diagonal_islands(self):
        """
        Test case with diagonal islands.
        Input: grid = [["1","0","0"], ["0","1","0"], ["0","0","1"]]
        Output: 3
        """
        grid = [["1", "0", "0"], ["0", "1", "0"], ["0", "0", "1"]]
        expected = 3
        self.assertEqual(expected, self.SUT(grid))

    def test_mixed_islands(self):
        """
        Test case with mixed islands.
        Input: grid = [["1","1","0","0"], ["1","0","0","1"], ["0","0","1","1"], ["1","0","0","1"]]
        Output: 5
        """
        grid = [["1", "1", "0", "0"], ["1", "0", "0", "1"], ["0", "0", "1", "1"], ["1", "0", "0", "1"]]
        expected = 5
        self.assertEqual(expected, self.SUT(grid))


if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=2, exit=False)
