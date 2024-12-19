# Quick Sort
# QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways.

# Always pick first element as pivot.
# Always pick last element as pivot (implemented below)

# The key process in quickSort is partition(). Target of partitions is, given an array and an element x of array as pivot, put x at its correct position in sorted array and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x. All this should be done in linear time.


def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)
        
    return arr

# Test the quick sort algorithm
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
print(f"Unsorted array: {arr}")
sorted_arr = quick_sort(arr, 0, n-1)
print(f"Sorted array: {sorted_arr}")

    
    