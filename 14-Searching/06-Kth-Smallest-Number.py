# Kth Smallest Numbers in Unsorted Array

# Given an unsorted array of numbers, find the ‘K’ smallest numbers in it.

def quickselect(array, k):
    # Write your code here.
    position = k-1
    return quickselectHelper(array,0,len(array)-1,position)


def quickselectHelper(array,startIdx,endIdx,position):
    while True:
        if startIdx > endIdx:
            raise Exception("Your algo should never come here")
        pivotIdx = startIdx
        leftIdx = startIdx+1
        rightIdx = endIdx

        while leftIdx <=rightIdx:
            if array[leftIdx]>array[pivotIdx] and array[rightIdx]<array[pivotIdx]:
                swap(leftIdx,rightIdx,array)
            if array[leftIdx]<=array[pivotIdx]:
                leftIdx+=1
            if array[rightIdx]>=array[pivotIdx]:
                rightIdx-=1
        swap(pivotIdx,rightIdx,array)
        if rightIdx == position:
            return array[rightIdx]
        elif rightIdx<position:
            startIdx = rightIdx+1
        else : endIdx = rightIdx-1
def swap(one, two,array):
    array[one],array[two]=array[two],array[one]
                
# Test the function

array = [1, 5, 12, 2, 11, 5]
k = 3

print(quickselect(array, k)) # [1, 2, 5]
# Time Complexity : O(n)
