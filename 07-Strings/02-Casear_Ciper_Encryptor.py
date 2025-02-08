#Caser Ciper Encryptor

def caserCipherEncryptor(string, key):
    newLetters = []
    newKey = key % 26
    for letter in string:
        newLetters.append(getNewLetter(letter, newKey))
    return "".join(newLetters)

def getNewLetter(letter, key):
    newLetterCode = ord(letter) + key
    return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 122)

# Test the caserCipherEncryptor function

string = "xyz"
key = 2
print(caserCipherEncryptor(string, key)) # zab

string = "abc"
key = 57
print(caserCipherEncryptor(string, key)) # fgh

# Time Complexity: O(n)
# Space Complexity: O(n)

