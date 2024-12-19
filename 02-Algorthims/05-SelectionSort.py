#Selection Sort 
#Selection Sort is the simplest sorting algorithm that works by repeatedly finding the minimum element from the unsorted part of the array and putting it at the beginning.

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Test the selection sort algorithm
arr = [64, 34, 25, 12, 22, 11, 90]
print(f"Unsorted array: {arr}")
sorted_arr = selection_sort(arr)
print(f"Sorted array: {sorted_arr}")

# Time Complexity of Selection Sort : O(n^2)
# Space Complexity of Selection Sort : O(1)
