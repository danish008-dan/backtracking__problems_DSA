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


Subsets (Power Set)
===================

Problem Description
-------------------
Given a list of distinct integers, generate all possible
subsets (the power set).

Each element can either be included or excluded.

Approach
--------
Backtracking is used to build subsets incrementally.
At each step:
- Add current subset to result
- Try including remaining elements one by one
- Backtrack after exploring each possibility

Key Concepts
------------
- Recursion
- Decision tree exploration
- Include / Exclude pattern

Time Complexity
---------------
O(2^n)

Space Complexity
----------------
O(n)

Applications
------------
- Combination generation
- Feature selection
- Search space explorati
-
-Backtracking Problems – Permutations and Rat in a Maze
=======================================================

1. Permutations
---------------

Problem:
Generate all possible arrangements of elements.

Approach:
Use backtracking with a boolean array to track
used elements. Choose → Explore → Undo.

Time Complexity:
O(n!)

Applications:
- Arrangement generation
- Scheduling problems
- Brute force search


2. Rat in a Maze
----------------

Problem:
Find a path in a binary maze from source to destination.

Approach:
Use backtracking to explore valid paths and mark
visited cells. If a path fails, backtrack and try
another direction.

Time Complexity:
O(2^(n^2)) worst case

Applications:
- Path finding
- Constraint solving
- AI search algorithms

-
-
- on
Sudoku Solver (Backtracking)
============================

Problem Description
-------------------
Solve a 9x9 Sudoku puzzle such that:
- Each row contains digits 1–9 exactly once.
- Each column contains digits 1–9 exactly once.
- Each 3x3 subgrid contains digits 1–9 exactly once.

Approach
--------
Backtracking is used to:
1. Find an empty cell.
2. Try digits 1–9.
3. Check if placement is valid.
4. Recursively solve the remaining board.
5. Undo the move if it leads to a dead end.

Key Concepts
------------
- Constraint satisfaction
- Recursive search
- State backtracking
- Pruning invalid states

Time Complexity
---------------
Worst case: O(9^(n*n))

Applications
------------
- Puzzle solvers
- AI search algorithms
- Constraint-based systems
