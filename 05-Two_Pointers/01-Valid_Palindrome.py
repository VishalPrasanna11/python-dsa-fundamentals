# Leetcode link: https://leetcode.com/problems/valid-palindrome/

# Problem:
# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Example 1:

# Input: s = "abacd"
# Output: false

# Example 2:

# Input: s = "abba"
# Output: true

# Constraints:

# 1 <= s.length <= 2 * 105

# s consists only of printable ASCII characters.

# Solution:

# Approach:

# 1. We will use two pointers, one at the start of the string and the other at the end of the string.
# 2. We will keep moving the pointers towards each other until they meet.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        start = 0
        end = len(s)-1
        while start<end:
            if not s[start].isalnum():
                start+=1
                continue
            if not s[end].isalnum():
                end-=1
                continue
            if s[start]!=s[end]:
                return False
            start+=1
            end-=1
        return True
    
# Test the solution

s = Solution()
print(s.isPalindrome("I am :IronnorI Ma, i")) # True

# Time Complexity: O(n)
# Space Complexity: O(1)





