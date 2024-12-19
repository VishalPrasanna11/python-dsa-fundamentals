# Arrays
# An array is a collection of items stored at contiguous memory locations. The idea is to store multiple items of the same type together. This makes it easier to calculate the position of each element by simply adding an offset to a base value, i.e., the memory location of the first element of the array (generally denoted by the name of the array).
# For simplicity, we can think of an array as a list of items. For example, an array of integers can look like this:
# [1, 2, 3, 4, 5]
# The above array can be thought of as a list of five integers. All the elements in the array are stored in contiguous memory locations. If we know the address of the first element, we can calculate the address of the other elements.

array = [1, 2, 3, 4, 5]
print(array)

# Accessing elements of an array
# The elements of an array can be accessed using an index. The index of an array starts at 0. For example, the first element of the array is accessed using the index 0, the second element using the index 1, and so on.

# Accessing the first element of the array
print(array[0])

# Time Complexity of accessing an element in an array: O(1)

# Inserting elements into an array
# Inserting an element into an array involves adding an element at a specific position in the array. The elements to the right of the inserted element are shifted to the right to accommodate the new element.

# Inserting an element at the end of the array
array.append(6)
print(array)

# Inserting an element at a specific position in the array

# Inserting 10 at index 2
array.insert(2, 10)
print(array)

# Time Complexity of inserting an element at the end of an array: O(1)
# Time Complexity of inserting an element at a specific position in an array: O(n)

# Deleting elements from an array
# Deleting an element from an array involves removing an element from a specific position in the array. The elements to the right of the deleted element are shifted to the left to fill the gap created by the deleted element.

# Deleting an element from the end of the array
array.pop()
print(array)

# Deleting an element from a specific position in the array
array.pop(2)
print(array)

# Time Complexity of deleting an element from the end of an array: O(1)
# Time Complexity of deleting an element from a specific position in an array: O(n)

# Searching for an element in an array
# Searching for an element in an array involves finding the position of the element in the array.

# for num in array:
#     if num == 3:
#         print(f"Element found at index {array.index(num)}")
#         break

# Time Complexity of searching for an element in an array: O(n)

# Updating an element in an array
# Updating an element in an array involves changing the value of an element at a specific position in the array.

# Updating the element at index 2
array[2] = 20
print(array)

# Time Complexity of updating an element in an array: O(1)

# Summary of Time Complexity of Array Operations
# Accessing an element in an array: O(1)
# Inserting an element at the end of an array: O(1)
# Inserting an element at a specific position in an array: O(n)
# Deleting an element from the end of an array: O(1)
# Deleting an element from a specific position in an array: O(n)
# Searching for an element in an array: O(n)
# Updating an element in an array: O(1)


