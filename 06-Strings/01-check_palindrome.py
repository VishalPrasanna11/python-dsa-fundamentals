# Check Palindrome


def check_palindrome(s):
    
    new_string = ""
    for char in s:
        new_string = char + new_string
        
    if s == new_string:
        return True
    else:
        return False
    
# check palindrome without using str
def check_palindrome_list(s):
   new_list = list(s)
   
   n = len(new_list)
   for char in s:
       new_list.insert(n, char)
       n -= 1
        
   if s == "".join(new_list):
        return True
    
print(check_palindrome_list("racecar")) #True


print(check_palindrome_list("hello")) #False
# Time Complexity: O(n)
# Space Complexity: O(n)

# Check Palindrome using Two Pointers

def check_palindrome_two_pointers(s):
    
    leftIdx = 0
    rightIdx = len(s) - 1
    
    while leftIdx < rightIdx:
        if s[leftIdx] != s[rightIdx]:
            return False
        leftIdx += 1
        rightIdx -= 1
        
    return True


print(check_palindrome_two_pointers("racecar")) #True
print(check_palindrome_two_pointers("hello")) #False

# Time Complexity: O(n)
# Space Complexity: O(1)