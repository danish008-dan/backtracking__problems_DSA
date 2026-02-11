N-Queens Problem (Backtracking)
================================

Problem Description
-------------------
Place N queens on an N x N chessboard such that
no two queens attack each other.

Queens attack:
- Same row
- Same column
- Same diagonal

Approach
--------
Backtracking is used to try placing a queen in each row.
If a placement is valid, move to the next row.
If not, backtrack and try a different column.

Key Concepts
------------
- Recursion
- Constraint checking
- Backtracking (undo previous decisions)

Time Complexity
---------------
O(N!)

Space Complexity
----------------
O(N^2)

Applications
------------
- Constraint satisfaction problems
- Puzzle solving
- AI search problems
