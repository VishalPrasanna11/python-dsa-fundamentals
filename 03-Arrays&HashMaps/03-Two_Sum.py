#Leetcode link: https://leetcode.com/problems/two-sum/

# Problem:
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        new_array ={}

      

        for i in range(len(nums)):
            diff = target- nums[i]

            if diff in new_array:
                return [new_array[diff],i]
            new_array[nums[i]] = i

        return []

# Test the solution
s = Solution()
print(s.twoSum([2,7,11,15],9)) # [0,1]
print(s.twoSum([3,2,4],6)) # [1,2]
print(s.twoSum([3,3],6)) # [0,1]
print(s.twoSum([3,2,3],6)) # [0,2]

# Time Complexity : O(n)
# Space Complexity : O(n)
# Explanation: We are iterating through the array and checking if the difference between the target and the current element is present in the hashmap. If it is present we return the indices of the current element and the difference. If it is not present we add the current element to the hashmap.