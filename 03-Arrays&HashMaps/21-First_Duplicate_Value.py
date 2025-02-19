# Difficulty: Easy
# First Duplicate Value
# Write a function that takes in an array of integers between 1 and n, where n is the length of the array, and returns the first integer that appears more than once (when the array is read from left to right).
# In other words, out of all the integers that might occur more than once in the input array, your function should return the one whose first duplicate value has the minimum index.
# If no integer appears more than once, your function should return -1.
# Note that you're allowed to mutate the input array.



def firstDuplicateValue(array):
    # Write your code here.

    new_set = set()
    for num in array:
        if num in new_set:
            return num
        new_set.add(num)
    return -1
 
