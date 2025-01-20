# Find the Digits in a Number

num = 1234567811111111


def findDigits(num,digits):
    
    #Termination Condition:
    
    if num == 0:
        return digits
    
    #base Condtion
    
    return findDigits(num//10,digits+1)


print(findDigits(num,0))
    