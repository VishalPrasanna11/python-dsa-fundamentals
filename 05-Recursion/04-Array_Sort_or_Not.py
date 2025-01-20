#Array Sorted or Not
#No Duplicates

arr = [1,2,3,4,5,6,7,8,9]

arr2 = [1,0,3,4,5,6,9,2]

def isSorted(arr, n):
    
    
    if n == len(arr):
        return True
    
    
    if arr[n]<arr[n-1]:
        return False
        
    
  
    return isSorted(arr,n+1)
    
print(isSorted(arr2,1))