# Maximum number in a Array 

arr = [1, 2, 3, 4, 5,6,7]

def maxNumber(arr, n, maxNum):
    
   
    #Base Condition
    if n == len(arr):
        return maxNum
    
    if arr[n]>maxNum:
        maxNum=arr[n]
        
        
    
    return maxNumber(arr,n+1,maxNum)
    

maxnum = maxNumber(arr,0,float('-inf'))

print(maxnum)
    