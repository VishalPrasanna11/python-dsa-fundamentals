# Product Sum
# Given an array of integers (where each integer is a positive integer itself), write a function that returns its product sum. The product sum of an array is the sum of its elements, where nested arrays should be summed themselves and then multiplied by their level of depth. For example, the product sum of [x, y] is x + y; the product sum of [x, [y, z]] is x + 2y + 2z.

# Sample Input
# array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
# Sample Output
# 12

def productSum(array,level=1):
    sum = 0
    for element in array:
        if type(element) is list:
            sum+=productSum(element,level+1)
        else:
            sum += element
    return sum*level


# Test
array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]

print(productSum(array)) # 12

# Test

array = [1, 2, 3, 4, 5]

print(productSum(array)) # 15