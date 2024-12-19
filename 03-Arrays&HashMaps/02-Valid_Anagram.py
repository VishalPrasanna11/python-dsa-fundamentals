# Leetcode: 242. Valid Anagram

# Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        char_count = {}
        for char in s:
            char_count[char]= char_count.get(char,0)+1

        for char in t:
            if char not in char_count:
                return False
            char_count[char]-=1
            if char_count[char]<0:
                return False
            
        return True


        
# Test the solution
s = Solution()
print(s.isAnagram("anagram","nagaram")) # True
print(s.isAnagram("rat","car")) # False
print(s.isAnagram("a","ab")) # False
print(s.isAnagram("aacc","ccac")) # False

# Time Complexity: O(n)
# Space Complexity: O(1)