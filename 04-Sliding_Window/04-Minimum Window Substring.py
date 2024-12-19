# Minimum Window Substring 

# Leetcode link: https://leetcode.com/problems/minimum-window-substring/

# Problem:
# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

from typing import List

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        # Dictionaries to store character counts
        tList, sList = {}, {}
        for char in t:
            tList[char] = tList.get(char, 0) + 1

        # Initialize variables for the sliding window
        left = 0
        min_length = float('inf')
        min_window = ""
        required = len(tList)  # Number of unique characters in t
        formed = 0  # To track how many characters meet the required count in the window

        for right in range(len(s)):
            # Add the current character to the window
            char = s[right]
            sList[char] = sList.get(char, 0) + 1

            # If the character is part of t and its count matches in sList and tList
            if char in tList and sList[char] == tList[char]:
                formed += 1

            # Try to shrink the window from the left
            while formed == required:
                # Update the minimum window if the current window is smaller
                window_length = right - left + 1
                if window_length < min_length:
                    min_length = window_length
                    min_window = s[left:right + 1]

                # Remove the leftmost character from the window
                left_char = s[left]
                sList[left_char] -= 1
                if left_char in tList and sList[left_char] < tList[left_char]:
                    formed -= 1
                left += 1

        return min_window

# Test the solution
s = Solution()
print(s.minWindow("ADOBECODEBANC", "ABC")) # "BANC"
print(s.minWindow("a", "a")) # "a"