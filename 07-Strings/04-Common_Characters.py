#Common Characters in a list of strings
# Given a list of strings, write a function that returns a list of characters that are common to all the strings in the list. If there are no common characters, return an empty list.


def commonCharacters(strings):
    # Write your code here.

    char_count = {}

    for char in strings:
        for s in set(char):
            char_count[s] = char_count.get(s, 0) + 1
                
            

    char_list = []

    n = len(strings)

    for key, value in char_count.items():
        if value>=n:
            char_list.append(key)
    return char_list


print(commonCharacters(["bella", "label", "roller"])) #['e', 'l']

print(commonCharacters(["cool", "lock", "cook"])) #['c', 'o']
