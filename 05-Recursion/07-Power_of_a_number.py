# Power of a Number 


num = 5

p = 2


def findPower(num, p):
    
    # termination Condition
    if p == 0:
        return 1
    
    
    #Base Condition
    
    return num*findPower(num, p-1)


print(findPower(num,p))
    
    