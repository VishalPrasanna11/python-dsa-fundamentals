#Bubble Sort
#Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.

#Example
#First Pass:
#( 5 1 4 2 8 ) –> ( 1 5 4 2 8 ), Here, algorithm compares the first two elements, and swaps since 5 > 1.
#( 1 5 4 2 8 ) –>  ( 1 4 5 2 8 ), Swap since 5 > 4
#( 1 4 5 2 8 ) –>  ( 1 4 2 5 8 ), Swap since 5 > 2
#( 1 4 2 5 8 ) –> ( 1 4 2 5 8 ), Now, since these elements are already in order (8 > 5), algorithm does not swap them.

#Second Pass:
#( 1 4 2 5 8 ) –> ( 1 4 2 5 8 )
#( 1 4 2 5 8 ) –> ( 1 2 4 5 8 ), Swap since 4 > 2
#( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
#( 1 2 4 5 8 ) –>  ( 1 2 4 5 8 )
#Now, the array is already sorted, but our algorithm does not know if it is completed. The algorithm needs one whole pass without any swap to know it is sorted.


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Test the bubble sort algorithm

arr = [64, 34, 25, 12, 22, 11, 90]
print(f"Unsorted array: {arr}")
sorted_arr = bubble_sort(arr)
print(f"Sorted array: {sorted_arr}")

# Time Complexity of Bubble Sort : O(n^2)
# Space Complexity of Bubble Sort : O(1)
# Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.

