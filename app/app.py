from flask import Flask, request, jsonify
from Solution import Solution

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

