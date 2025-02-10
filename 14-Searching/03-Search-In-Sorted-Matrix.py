# Sorted Matrix Search

# Given a matrix mat[] of size n x m, where every row and column is sorted in increasing order, and a number x is given. The task is to find whether element x is present in the matrix or not.

def searchInSortedMatrix(matrix, target):
    # Write your code here.
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == target:
                return [i,j]
    return [-1,-1]


matrix = [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004]
]

target = 44

print(searchInSortedMatrix(matrix, target)) # [3, 3]

# Time Complexity : O(n*m)
# Space Complexity : O(1)

# Optimized Solution

def searchInSortedMatrix2(matrix, target):
    # Write your code here.
    row = 0
    col = len(matrix[0])-1

    while row < len(matrix) and col >= 0:
        if matrix[row][col]>target:
            col -=1
        elif matrix[row][col]<target:
            row+=1
        else: 
            return [row,col]

    return [-1,-1]


matrix = [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004]
]

target = 44

print(searchInSortedMatrix2(matrix, target)) # [3, 3]

# Time Complexity : O(n+m)
# Space Complexity : O(1)