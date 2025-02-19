# Difficulty: Medium
# Move the elements to the end of the array

# You're given an array of integers and an integer. Write a function that moves all instances of that integer in the array to the end of the array and returns the array.


def moveElementToEnd(array, toMove):
    # Write your code here.
    i = 0
    j = len(array)-1

    while i < j :
        while i < j and array[j] == toMove:
            j-=1
        if array[i] == toMove:
            array[i],array[j] = array[j],array[i]

        i += 1
    return array
