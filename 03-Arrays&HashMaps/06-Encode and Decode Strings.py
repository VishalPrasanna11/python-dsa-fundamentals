# Leetcode link: https://leetcode.com/problems/encode-and-decode-strings/
# Problem:
# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

from typing import List
class Solution:

    def encode(self, strs: List[str]) -> str:
        # Concatenate the length of each string followed by the string itself
        single_str = ''
        for s in strs:
            single_str += str(len(s)) + '#' + s  # Use '#' as a delimiter between length and string
    
        return single_str

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        
        strs = []
        i = 0
        while i < len(s):
            # Find the length of the next string
            length = 0
            while s[i].isdigit():
                length = length * 10 + int(s[i])  # Construct the length from the digits
                i += 1
            
            # Skip the delimiter '#'
            i += 1
            
            # Get the string of the given length
            strs.append(s[i:i + length])
            i += length  # Move past the string
            
        return strs
