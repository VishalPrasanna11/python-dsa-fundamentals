#Generate Document
# You're given a string of available characters and a string representing a document that you need to generate. Write a function that determines if you can generate the document using the available characters. If you can generate the document, your function should return true; otherwise, it should return false.

def generateDocument(characters, document):
    # Write your code here.

    char_list = {}

    for char in characters:
        char_list[char]=char_list.get(char,0)+1

    for char in document:
        if char not in char_list:
            return False
        else:
            char_list[char]-=1
            if char_list[char]==0:
                del char_list[char]

            
    return True

#Small Optimization 
def generateDocument1(characters, document):
    char_list = {}
    
    for char in characters:
        char_list[char]=char_list.get(char,0)+1
        
    for char in document:
        if char not in char_list or char_list[char]==0:
            return False
        char_list[char]-=1
    
    return True


#Time Complexity: O(n+m)
#Space Complexity: O(c)

print(generateDocument("Bste!hetsi ogEAxpelrt x ", "AlgoExpert is the Best!")) #True
print(generateDocument("Bste!hetsi ogEAxpelrt x ", "AlgoExpert is the Best")) #False
print(generateDocument("abcabc","aabbccc")) #True

print(generateDocument1("Bste!hetsi ogEAxpelrt x ", "AlgoExpert is the Best!")) #True
print(generateDocument1("Bste!hetsi ogEAxpelrt x ", "AlgoExpert is the Best")) #False
print(generateDocument1("abcabc","aabbccc")) #True
