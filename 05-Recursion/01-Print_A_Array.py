#Print a array using recursion


# Define a array 
arr = [1, 2, 3, 4, 5,6,7]

# Output: 1 2 3 4 5


def printArray(arr, n):
    
    # Base case 
    if n == len(arr):
        print()
        return
    
    print(arr[n], end=" ")
    
    # Recursive case
    
    printArray(arr, n+1)
    
printArray(arr, 0)

