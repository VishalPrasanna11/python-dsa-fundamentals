def reverseWordsInString(string):
    # Write your code here.
    words = []
    startOfIndex = 0

    for i in range(len(string)):
        char = string[i]

        if char ==" ":
            words.append(string[startOfIndex:i])
            startOfIndex = i
        elif string[startOfIndex] == " ":
            words.append(" ")
            startOfIndex = i

    words.append(string[startOfIndex:])
    reverseList(words)    
    
    return "".join(words)


def reverseList(words):
    left  = 0
    right = len(words)-1

    while left<right:
        words[left],words[right] =  words[right],words[left]
        left+=1
        right-=1
        
        
# Test the reverseWordsInString function

print(reverseWordsInString("AlgoExpert is the best!")) #best! the is AlgoExpert