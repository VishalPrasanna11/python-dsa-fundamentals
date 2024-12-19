# Source: https://leetcode.com/problems/top-k-frequent-elements/

# Problem:
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashMap = {}

        for num in nums:
            hashMap[num]= hashMap.get(num,0)+1
        
        sorted_dict = sorted(hashMap.items(), key=lambda item: item[1], reverse = True)
            
        ans = [item[0] for item in sorted_dict[:k]]
        return ans

# Test the solution

s = Solution()
print(s.topKFrequent([1,1,1,2,2,3],2)) # [1,2]
print(s.topKFrequent([1],1)) # [1]
print(s.topKFrequent([1,2],1)) # [1]
print(s.topKFrequent([1,2,3],1)) # [1]

# Time Complexity: O(nlogn)
# Space Complexity: O(n)