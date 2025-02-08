#Longest Plaindrome in a String
#Given a string S, find the longest palindromic substring in S.

# Substring: A substring is a contiguous sequence of characters within a string. For example, "bcd" is a substring of "abcde" but "ace" is not a substring of "abcde".

# Palindrome: A palindrome is a string that reads the same backward as forward. For example, "madam" is a palindrome, but "ab" is not a palindrome.
def longestPalindromicSubstring(string):
    # Write your code here.
    longest = ""
    for i in range(len(string)):
        for j in range(i,len(string)):
            substring = string[i:j+1]
            if checkpalindrome(substring) and len(substring) >len(longest):
                longest = substring
    return longest


def checkpalindrome(s:str)->str:
    left =0
    right= len(s)-1

    while left <right:
        if s[left]!=s[right]:
            return False
        left+=1
        right-=1

    return True


# Time Complexity: O(n^3)

def longestPalindromicSubstring2(string):
    # Write your code here.
    current_longest = [0,1] #Index 0

    for i in range(1,len(string)):
        odd = getLargestPalindrome(string,i-1,i+1)
        even = getLargestPalindrome(string,i-1,i)

        largest = max(odd,even,key = lambda x:x[1]-x[0])
        current_longest = max(largest,current_longest,key=lambda x : x[1]-x[0])
    return string[current_longest[0]:current_longest[1]]
        

def getLargestPalindrome(string,left,right):
    while left>=0 and right <len(string):
        if string[left]!=string[right]:
            break

        left -=1
        right+=1
    return [left+1,right]

# Time Complexity: O(n^2)

# Test the longestPalindromicSubstring function
print(longestPalindromicSubstring("babad")) #aba
print(longestPalindromicSubstring("cbbd")) #bb
print(longestPalindromicSubstring("a")) #a
print(longestPalindromicSubstring("ac")) #a
print(longestPalindromicSubstring("bb")) #bb

print(longestPalindromicSubstring2("babad")) #aba
print(longestPalindromicSubstring2("cbbd")) #bb
print(longestPalindromicSubstring2("a")) #a
print(longestPalindromicSubstring2("ac")) #a
print(longestPalindromicSubstring2("bb")) #bb
