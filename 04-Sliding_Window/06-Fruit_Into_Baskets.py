# Fruit into Baskets
# leetcode link: https://leetcode.com/problems/fruit-into-baskets/

# Problem:
# You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.
from typing import List
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        fruit_basket = {}

        max_fruits = 0
        left = 0
       
        for right in range(len(fruits)):
            fruit_basket[fruits[right]] = fruit_basket.get(fruits[right], 0)+1

            while len(fruit_basket)>2:
                fruit_basket[fruits[left]]-=1
                if fruit_basket[fruits[left]] == 0:
                    del fruit_basket[fruits[left]]
                left+=1

            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits
        
# Test the solution

s = Solution()
print(s.totalFruit([1,2,1])) # 3
print(s.totalFruit([0,1,2,2])) # 3

