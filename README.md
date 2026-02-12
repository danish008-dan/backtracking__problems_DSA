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
