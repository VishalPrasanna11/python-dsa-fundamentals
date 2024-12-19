#Linear Search Algorithm

# Linear search is a simple search algorithm with run-time complexity of Ο(n).

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

#Conditions for the linear search
# 1. The array must be indexed
# 2. The array must be of a fixed size
# 3. The array must be of a homogeneous data type

# Test the linear search algorithm
arr = [2, 3, 4, 10, 40]
x = 10

result = linear_search(arr, x)

# Print the result
if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")
    
