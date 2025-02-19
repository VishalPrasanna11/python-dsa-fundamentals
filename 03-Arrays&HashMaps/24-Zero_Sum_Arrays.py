# Difficulty: Easy
# Zero Sum Subarray
# Write a function that takes in an array of integers and returns a boolean representing whether the array contains a subarray that sums up to 0.


def zeroSumSubarray(nums):
    # Write your code here.

    sums = set([0])
    currentSum = 0

    for num in nums:
        currentSum += num
        if currentSum in sums:
            return True

        sums.add(currentSum)
    return False
