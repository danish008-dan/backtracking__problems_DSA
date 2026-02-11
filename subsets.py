"""
Purpose:
--------
Generate all possible subsets (power set)
of a given list using Backtracking.

Each element can either be included or excluded.
"""

def generate_subsets(nums):
    result = []

    # Backtracking function
    def backtrack(start, current_subset):
        # Add a copy of current subset to result
        result.append(current_subset[:])

        # Explore further elements
        for i in range(start, len(nums)):
            # Include nums[i]
            current_subset.append(nums[i])

            # Move to next element
            backtrack(i + 1, current_subset)

            # Backtrack (remove last element)
            current_subset.pop()

    backtrack(0, [])
    return result


# Example
nums = [1, 2, 3]
subsets = generate_subsets(nums)

for s in subsets:
    print(s)
