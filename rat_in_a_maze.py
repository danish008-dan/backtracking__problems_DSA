"""
Purpose:
--------
Solve the Rat in a Maze problem using Backtracking.

Find a path from top-left corner (0,0) to
bottom-right corner (n-1,n-1) in a binary maze.

1 = open path
0 = blocked cell
"""

def solve_maze(maze):
    n = len(maze)
    solution = [[0 for _ in range(n)] for _ in range(n)]

    def is_safe(x, y):
        return 0 <= x < n and 0 <= y < n and maze[x][y] == 1

    def backtrack(x, y):
        # If destination reached
        if x == n - 1 and y == n - 1:
            solution[x][y] = 1
            return True

        if is_safe(x, y):
            solution[x][y] = 1

            # Move Down
            if backtrack(x + 1, y):
                return True

            # Move Right
            if backtrack(x, y + 1):
                return True

            # Backtrack (unmark path)
            solution[x][y] = 0

        return False

    if backtrack(0, 0):
        return solution
    else:
        return "No path found"


maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]

result = solve_maze(maze)

for row in result:
    print(row)
