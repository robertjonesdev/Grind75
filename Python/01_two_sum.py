# Two Sum

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# https://leetcode.com/problems/two-sum/submissions/1254849811/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}

        for index, num in enumerate(nums):
            if target - num in complements:
                return complements[target - num], index
            else:
                complements[num] = index
