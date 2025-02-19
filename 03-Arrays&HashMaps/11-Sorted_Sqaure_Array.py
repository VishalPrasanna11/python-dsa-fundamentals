# The problem is asking to return the sorted square of the given array.

def sortedSquaredArray(array):
    # Write your code here.
    sortedSqaure = [0 for _ in array]

    for idx in range(len(array)):
        value = array[idx]
        sortedSqaure[idx] = value * value

    sortedSqaure.sort()
    return sortedSqaure
