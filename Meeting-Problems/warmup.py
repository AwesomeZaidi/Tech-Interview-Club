# Tech Interview Club Meeting Problems 06/06/19
# Overview: Easy / Medium Array Manipulation


# WARMUP PROBLEM:
# Given a sequence of consecutive integers, find the sum of all numbers


# PROBLEM 1:
# Say that a "clump" in an array is a series of 2 or more adjacent elements of the same value.
# Return the number of clumps in the given array.

# countClumps([1, 2, 2, 3, 4, 4]) → 2
# countClumps([1, 1, 2, 1, 1]) → 2
# countClumps([1, 1, 1, 1, 1]) → 1


# PROBLEM 2:
# Return an array that contains exactly the same numbers as the given array, but rearranged
# so that every 3 is immediately followed by a 4.
# Do not move the 3's, but every other number may move.
# The array contains the same number of 3's and 4's, every 3 has a number after it that
# is not a 3, and a 3 appears in the array before any 4.

# fix34([1, 3, 1, 4]) → [1, 3, 4, 1]
# fix34([1, 3, 4, 1, 4, 3, 1]) → [1, 3, 4, 1, 1, 3, 4]
# fix34([3, 2, 2, 4]) → [3, 4, 2, 2]


# PROBLEM 3:
# Given an array, rotate the array to the right by k steps, where k is non-negative.

# Input: [1,2,3,4,5,6,7] and k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# Input: [-1,-100,3,99] and k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
# Could you do it in-place with O(1) extra space?
