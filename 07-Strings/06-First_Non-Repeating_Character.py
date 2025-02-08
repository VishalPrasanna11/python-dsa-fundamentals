# Firsdef firstNonRepeatingCharacter(string):
    # Write your code here.

def firstNonRepeatingCharacter(string):
    # Write your code here.

    char_list = {}

    for char in string:
        char_list[char]=char_list.get(char,0)+1

    for i in range(len(string)):

        if char_list.get(string[i])==1:
            return i
            
    return -1



