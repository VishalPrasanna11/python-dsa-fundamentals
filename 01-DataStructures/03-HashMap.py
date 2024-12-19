# Dictory is a collection of key-value pairs
#  Its also called a hash map

# Creating a dictionary
# A dictionary is created by placing items inside curly braces {} separated by commas

# Creating an empty dictionary
my_dict = {}
print(my_dict)

# Creating a dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}
print(my_dict)

# Creating a dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}
print(my_dict)

# Adding elements to a dictionary

# Adding an element to an empty dictionary
my_dict = {}
my_dict[0] = 'apple'
print(my_dict)

# Adding an element to a non-empty dictionary

# Adding an element to a dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}

# Adding an element with key 3 and value 'cat'
my_dict[3] = 'cat'
print(my_dict)

# Deleting elements from a dictionary

del my_dict[1]
print(my_dict)

# Deleting an element from a dictionary using the pop() method
my_dict.pop(2)
print(my_dict)

# Deleting all elements from a dictionary using the clear() method

my_dict.clear()

# Deleting the dictionary using the del keyword
del my_dict

# Accessing elements from a dictionary

# Accessing an element using a key
my_dict = {1: 'apple', 2: 'ball'}

# Accessing the element with key 1
print(my_dict[1])

# Accessing an element using the get() method

# Accessing the element with key 2

print(my_dict.get(2))

# Accessing an element that does not exist in the dictionary
# Accessing an element with key 3
# print(my_dict[3])
# print(my_dict.get(3))

# Summary of dictionary operations

# Creating a dictionary : Time Complexity - O(1)
# Adding an element to a dictionary : Time Complexity - O(1)
# Deleting an element from a dictionary : Time Complexity - O(1)
# Accessing an element from a dictionary : Time Complexity - O(1)
# Searching for an element in a dictionary : Time Complexity - O(1)

