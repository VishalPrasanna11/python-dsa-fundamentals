# Inseration Sort
# Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands.

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return

# Test the insertion sort algorithm
arr = [12, 11, 13, 5, 6]
print(f"Unsorted array: {arr}")
insertion_sort(arr)
print(f"Sorted array: {arr}")

# Time Complexity of Insertion Sort : O(n^2)
# Space Complexity of Insertion Sort : O(1)
