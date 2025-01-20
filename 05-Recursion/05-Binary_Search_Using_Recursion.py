#Binary Search using Recursion


arr = [1,2,3,4,5,6,7,8,9,10]

target = 80

def BinarySearch(arr, n,target):
    
    #Termination Condition
    
    if n == len(arr):
        return False
    
    if arr[n]==target:
        return True
    
    
    return BinarySearch(arr,n+1,target)


print(BinarySearch(arr,0,target))