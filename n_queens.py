"""
Purpose:
--------
Solve the N-Queens problem using Backtracking.

Place N queens on an N x N chessboard such that
no two queens attack each other.

Constraints:
- Only one queen per row
- Only one queen per column
- No two queens share the same diagonal
"""

def solve_n_queens(n):
    # Initialize empty board
    board = [["." for _ in range(n)] for _ in range(n)]
    solutions = []

    # Function to check if placing queen is safe
    def is_safe(row, col):
        # Check column
        for i in range(row):
            if board[i][col] == "Q":
                return False

        # Check left diagonal
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        # Check right diagonal
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == "Q":
                return False
            i -= 1
            j += 1

        return True

    # Backtracking function
    def backtrack(row):
        # If all queens placed
        if row == n:
            solutions.append(["".join(r) for r in board])
            return

        for col in range(n):
            if is_safe(row, col):
                # Place queen
                board[row][col] = "Q"

                # Move to next row
                backtrack(row + 1)

                # Backtrack (remove queen)
                board[row][col] = "."

    backtrack(0)
    return solutions


# Example
solutions = solve_n_queens(4)

for sol in solutions:
    for row in sol:
        print(row)
    print()
