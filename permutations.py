"""
Purpose:
--------
Generate all possible permutations of a given list
using Backtracking.

Each element must appear exactly once in every permutation.
"""

def generate_permutations(nums):
    result = []

    def backtrack(current_permutation, used):
        # If permutation is complete
        if len(current_permutation) == len(nums):
            result.append(current_permutation[:])
            return

        for i in range(len(nums)):
            # Skip already used elements
            if used[i]:
                continue

            # Choose element
            used[i] = True
            current_permutation.append(nums[i])

            # Explore further
            backtrack(current_permutation, used)

            # Backtrack (undo choice)
            current_permutation.pop()
            used[i] = False

    used = [False] * len(nums)
    backtrack([], used)
    return result


# Example
nums = [1, 2, 3]
perms = generate_permutations(nums)

for p in perms:
    print(p)
