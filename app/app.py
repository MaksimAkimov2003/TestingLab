from typing import List

from flask import Flask, request, jsonify


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        islands = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if (
                r not in range(rows)
                or c not in range(cols)
                or grid[r][c] == "0"
                or (r, c) in visit
            ):
                return

            visit.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    islands += 1
                    dfs(r, c)
        return islands

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the homepage!"

@app.route('/num_islands', methods=['POST'])
def num_islands():
    data = request.get_json()
    grid = data.get('grid')

    # Validate grid
    if not isinstance(grid, list) or any(not isinstance(row, list) for row in grid):
        return jsonify({'error': 'Invalid grid format'}), 400
    for row in grid:
        for cell in row:
            if cell not in ['0', '1']:
                return jsonify({'error': 'Invalid cell value'}), 400

    try:
        solution = Solution()
        result = solution.numIslands(grid)
        return jsonify({'num_islands': result})
    except RecursionError:
        return jsonify({'error': 'Recursion limit exceeded'}), 500

