# Best Time to buy and sell stock
# Leetcode link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Problem:
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left = 0
        right = 1

        max_profit = 0

        while right < len(prices):
            if prices[right] > prices[left]:
                cur_profit = prices[right] - prices[left]
                max_profit = max(max_profit, cur_profit)  # Update max_profit
            else:
                left = right  # Update left pointer to the current right

            right += 1  # Move the right pointer to the next day

        return max_profit
