# Search in a Sorted Range

# Given a sorted array of integers, find the starting and ending position of a given target value. Your algorithm's runtime complexity must be in the order of O(log n). If the target is not found in the array, return [-1, -1].

# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

def searchForRange(array, target):
    # Write your code here.
    finalRange = [-1,-1]
    searchforRangeHelper(array,target,0,len(array)-1,finalRange,True)
    searchforRangeHelper(array,target,0,len(array)-1,finalRange,False)
    return finalRange


def searchforRangeHelper(array,target,left,right,finalRange,goLeft):
    if left>right:
        return

        
    mid = (left+right)//2
    match = array[mid]
    if match<target:
        searchforRangeHelper(array,target,mid+1,right,finalRange,goLeft)
    elif match>target:
            searchforRangeHelper(array,target,left,mid-1,finalRange,goLeft)
    else :
        if goLeft:
            if mid == 0 or array[mid-1]!=target:
                finalRange[0] = mid
            else:
                searchforRangeHelper(array,target,left,mid-1,finalRange,goLeft)
        else:
            if mid == len(array)-1 or array[mid+1]!=target:
                finalRange[1] = mid
            else:
                searchforRangeHelper(array,target,mid+1,right,finalRange,goLeft)
                
    
# Test the function

array = [5,7,7,8,8,10]

target = 8

print(searchForRange(array, target)) # [3,4]

array = [5,7,7,8,8,10]

target = 6

# Time Complexity : O(log n)
# Space Complexity : O(n)