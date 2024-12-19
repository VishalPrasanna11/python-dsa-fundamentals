# Leetcode link: https://leetcode.com/problems/contains-duplicate/

# Problem:
# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        hashMap = {}

        for num in nums:
            if num in hashMap:
                return True
            
            hashMap[num]=True
        
        return False
    
# Test the solution
s = Solution()
print(s.containsDuplicate([1,2,3,1])) # True
print(s.containsDuplicate([1,2,3,4])) # False
print(s.containsDuplicate([1,1,1,3,3,4,3,2,4,2])) # True
