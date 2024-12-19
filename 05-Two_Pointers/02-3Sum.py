# 3 Sum Problem
# Leetcode link: https://leetcode.com/problems/3sum/

# Problem:
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        
        nums.sort() # O(nlogn)
        
        for i in range (len(nums)-2): # O(n)
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left = i+1
            right = len(nums)-1
            
            while left < right:
               total = nums[i] + nums[left] + nums[right]
             
               if total==0:
                    ans.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left < right and nums[left] == nums[left-1]:
                        left+=1
                    while left < right and nums[right] == nums[right+1]:
                        right-=1
            
               elif total < 0:
                left+=1
               else:
                right-=1
                
        
        
        return ans
    
    
# Test the solution

s = Solution()

print(s.threeSum([-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]]

print(s.threeSum([])) # []

print(s.threeSum([0])) # []

# Time Complexity: O(n^2)
# Space Complexity: O(1)