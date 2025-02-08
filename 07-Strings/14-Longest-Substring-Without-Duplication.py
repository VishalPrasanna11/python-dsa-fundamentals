# Longest-Substring Without Duplication

# You're given a string of characters. You need to find the length of the longest substring that contains no repeated characters.

def longestSubstringWithoutDuplication(string):
    lastSeen = {}
    longest = [0,1]
    left = 0
    for i, char in enumerate(string):
        if char in lastSeen:
            left = max(left,lastSeen[char]+1)
        if longest[1] - longest[0]<i+1 - left:
            longest = [left,i+1]
        lastSeen[char]=i
    return string[longest[0]:longest[1]]


#Time Complexity: O(n)

#Space Complexity: O(min(n,a)) where n is the length of the string and a is the number of unique characters in the string

#Test the longestSubstringWithoutDuplication function

print(longestSubstringWithoutDuplication("clementisacap")) #clementisa
print(longestSubstringWithoutDuplication("abcdeabcdefc")) #abcdef
print(longestSubstringWithoutDuplication("abacacacaaabacaaaeaaafa")) #bac
print(longestSubstringWithoutDuplication("abcdeabcdefc")) #abcdef
