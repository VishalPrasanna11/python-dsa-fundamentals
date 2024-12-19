# Binary Serach Algorithm
#  Binary search is a fast search algorithm with run-time complexity of Ο(log n).


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1

        # x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return -1

#Conditions for the binary search
# 1. The array must be sorted
# 2. The array must be indexed
# 3. The array must be of a fixed size
# 4. The array must be of a homogeneous data type


# Test the binary search algorithm
arr = [2, 3, 4, 10, 40]
x = 10
result = binary_search(arr, x)

# Print the result
if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")
    

# Time Complexity of Binary Search : O(log n)
# Space Complexity of Binary Search : O(1)


