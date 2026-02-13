"""
Purpose:
--------
Solve a 9x9 Sudoku puzzle using Backtracking.

Rules:
- Each row must contain digits 1–9 without repetition.
- Each column must contain digits 1–9 without repetition.
- Each 3x3 subgrid must contain digits 1–9 without repetition.

Empty cells are represented by 0.
"""

def solve_sudoku(board):

    # Check if placing num at position (row, col) is valid
    def is_valid(row, col, num):

        # Check row
        for c in range(9):
            if board[row][c] == num:
                return False

        # Check column
        for r in range(9):
            if board[r][col] == num:
                return False

        # Check 3x3 subgrid
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3

        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):
                if board[r][c] == num:
                    return False

        return True

    # Backtracking function
    def backtrack():
        for row in range(9):
            for col in range(9):

                # If empty cell found
                if board[row][col] == 0:

                    # Try numbers 1 to 9
                    for num in range(1, 10):

                        if is_valid(row, col, num):
                            board[row][col] = num

                            # Recursively attempt to fill rest
                            if backtrack():
                                return True

                            # Backtrack (undo assignment)
                            board[row][col] = 0

                    return False

        # If no empty cell left, puzzle solved
        return True

    backtrack()
    return board


# Example Sudoku board
board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

solution = solve_sudoku(board)

for row in solution:
    print(row)
