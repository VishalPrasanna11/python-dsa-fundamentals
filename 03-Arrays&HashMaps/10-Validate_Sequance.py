# Write a function that takes in two non-empty arrays of integers, and returns a boolean representing whether the second array is a subsequence of the first one.
# Complexity: O(n) time | O(1) space
def isValidSubsequence(array, sequence):
    # Write your code here.
    arrIdx = 0
    seqIdx = 0
    while arrIdx <len(array) and seqIdx < len(sequence):
        if array[arrIdx]==sequence[seqIdx]:
            seqIdx += 1
            
        arrIdx += 1

    return seqIdx == len(sequence)
