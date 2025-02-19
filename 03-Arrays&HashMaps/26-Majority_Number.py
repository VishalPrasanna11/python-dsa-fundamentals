# Majority Number
# Time: O(n) | Space: O(1)

def majorityElement(array):
    # Write your code here.
    count = 0
    answer = None 

    for num in array:
        if count == 0:
            answer = num

        if num == answer:
            count+=1
        else:
            count -=1

    return answer
            
