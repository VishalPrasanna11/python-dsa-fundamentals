#Minimum Number in Arrray


arr = [0, -1, 2, 3, -4, -1, 10, 110, -100]


def minNum(arr, n, minNumber):
    
    # Base Condition 
    if n == len(arr):
        return minNumber
    
    
    #Condtion 
    if arr[n]< minNumber:
        minNumber= arr[n]
        
    return minNum(arr, n+1, minNumber)


minnum = minNum(arr, 0 , 0)

print(minnum)