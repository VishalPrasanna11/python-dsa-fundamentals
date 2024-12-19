# Leetcode link: https://leetcode.com/problems/product-of-array-except-self/

# Problem:
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1]*n

        left_product = 1
        for i in range(len(nums)):
            result[i]=left_product
            left_product*=nums[i]


        right_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]

        return result


# Test the solution
s = Solution()

print(s.productExceptSelf([1,2,3,4])) # [24,12,8,6]

# Time Complexity: O(n)

# Space Complexity: O(1)