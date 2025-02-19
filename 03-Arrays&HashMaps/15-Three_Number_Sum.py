# Three Number Sum
# Time: O(n^2) | Space: O(n)

def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    triplets = []
    
    for i in range(len(array)-2):
        left = i+1
        right = len(array)-1
        while left < right:
            cu_sum = array[i] + array[left] + array[right]
            if cu_sum == targetSum:
                triplets.append([array[i],array[left],array[right]])
                left+=1
                right-=1
            elif cu_sum< targetSum:
                 left+=1
            else : 
                right-=1
    return triplets

