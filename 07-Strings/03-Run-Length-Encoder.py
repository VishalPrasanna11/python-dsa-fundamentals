#Run Length Codeing

# Given a string, Your task is to write a function to perform basic string compression using the counts of repeated characters. This will be done by replacing the repeated characters with character followed by the count of the character. For example, if the string is aabbbcc, then the output should be a2b3c2.
# Special Note: You can assume that the input string has only uppercase and lowercase letters (a-z).
# You can count only the 9 consecutive repeated characters. For example, if the input string is aaaaaaaaaaaabbbbbbbbbbbbbbb, then the output should be a9a4b14.

def runLengthEncoding(string):
    # Write your code here.

    char_list = []
    count =1

    for i in range(1,len(string)):
        if  count == 9 or string[i]!=string[i-1]:
            char_list.append(str(count))
            char_list.append(string[i-1])
            count =0

        count+=1
    char_list.append(str(count))
    char_list.append(string[len(string)-1])

    return "".join(char_list)
      


print(runLengthEncoding("aabbbcc")) #a2b3c2
print(runLengthEncoding("aaaaaaaaaaabbbbbbbbbbbbbbb")) #a9a4b14