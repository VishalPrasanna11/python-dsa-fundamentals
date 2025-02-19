# Two Number Sum

def twoNumberSum(array, targetSum):
    # Write your code here.
    nums = {}
    for num in array:
        potentionalMatch = targetSum - num
        if potentionalMatch in nums:
            return [potentionalMatch,num]
        else :
                nums[num] = True
    return []
