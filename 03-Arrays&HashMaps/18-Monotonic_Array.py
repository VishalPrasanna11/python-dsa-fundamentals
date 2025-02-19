# Difficulty: Easy
# Monotonic Array
# Write a function that takes in an array of integers and returns a boolean representing whether the array is monotonic.


def isMonotonic(array):
    # Write your code here.

    isIncrease = True
    isDecrease = True

    for i in range(1,len(array)):
        if array[i] > array[i-1]:
            isDecrease = False
        if array[i] < array [i-1]:
            isIncrease = False
    
    return isIncrease or isDecrease
