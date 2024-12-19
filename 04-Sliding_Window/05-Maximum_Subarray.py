# Maximum Subarray

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        currentSum=nums[0]
        max_sum = nums[0]

        for num in nums[1:]:

            currentSum = max(num,currentSum+num)

            if(currentSum>max_sum):
                max_sum = currentSum


        return max_sum
        

# Test the solution

s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # 6
print(s.maxSubArray([1])) # 1
