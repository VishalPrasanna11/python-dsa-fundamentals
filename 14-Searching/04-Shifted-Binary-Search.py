# Shifted Binary Search
# Given a sorted array of integers that has been rotated a number of times, write a function that finds an element in the array. You may assume that the array was originally sorted in increasing order.

# The shifted binary search algorithm can be used to solve this problem. The algorithm is similar to the binary search algorithm, but with a few modifications. The algorithm works as follows:


def shiftedBinarySearch(array, target):
    # Write your code here.

    return shiftedBinarySearchHelper(array,target,0,len(array)-1)

def shiftedBinarySearchHelper(array,target,left,right):
    if left > right:
        return -1
    middle = (left+right)//2
    match = array[middle]
    leftNum = array[left]
    rightNum = array[right]
    if target == match:
        return middle
    elif leftNum<=match:
        if target<match and target>=leftNum:
            return shiftedBinarySearchHelper(array,target,left,middle-1)
        else:
            return shiftedBinarySearchHelper(array,target,middle+1,right)
    else : 
        if target > match and target <= rightNum:
            return shiftedBinarySearchHelper(array,target,middle+1,right)
        else:
            return shiftedBinarySearchHelper(array,target,left,middle-1)


# Test the function

array = [45, 61, 71, 72, 73, 0, 1, 21, 33, 37]
target = 33

print(shiftedBinarySearch(array, target)) # 8

array = [45, 61, 71, 72, 73, 0, 1, 21, 33, 37]
target = 61

print(shiftedBinarySearch(array, target)) # 1

# Time Complexity : O(log n)
# Space Complexity : O(log n)