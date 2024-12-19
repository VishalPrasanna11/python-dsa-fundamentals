#Longest Consecutive Sequence
# Leetcode link: https://leetcode.com/problems/longest-consecutive-sequence/

# Problem:
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
      hashMap = {num : False for num in nums}
      

      if len(nums)==0:
        return 0
      elif  len(nums)==1:
        return 1
      
      longest = 1
      
      for num in nums:

        curr=1
        nextNum = num+1

        while(nextNum in hashMap and hashMap[nextNum]==False):
            curr+=1
            hashMap[nextNum]=True
            nextNum+=1
        
        preNum= num-1

      
        while(preNum in hashMap and hashMap[preNum]==False):
            curr+=1
            hashMap[preNum]=True
            preNum-=1
        
        if(longest<curr):
            longest = curr
      

      return longest


# Test the solution
s = Solution()
print(s.longestConsecutive([100,4,200,1,3,2])) # 4
print(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1])) # 9

# Time Complexity: O(n)
# Space Complexity: O(n)

