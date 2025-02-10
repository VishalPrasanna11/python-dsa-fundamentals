def findThreeLargestNumbers(array):
    # Write your code here.
    threeLargest = [None,None,None]

    for num in array:
        updateLargest(threeLargest,num)

    return threeLargest

def updateLargest(array,num):

    if array[2] is None or num > array[2]:
        shiftAndUpdate(array,num,2)
    elif array[1] is None or num > array[1]:
        shiftAndUpdate(array,num,1)
    elif array[0] is None or num > array[0]:
          array[0]=num


def shiftAndUpdate(array,num,idx):
    for i in range(idx+1):
        if i == idx:
            array[i]=num
        else:
            array[i]=array[i+1]
    
        
# Test the function

array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
print(findThreeLargestNumbers(array)) # [18, 141, 541]

array = [55, 7, 8]
print(findThreeLargestNumbers(array)) # [7, 8, 55]


# Time Complexity : O(n)