#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

from typing import *  # type: ignore

# @lc code=start


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        print(str(prices))
        maxprofit = 0
        left = 0
        right = 1
        while right < len(prices) and left < len(prices):
            profit = prices[right] - prices[left]
            if profit <= 0:
                left = right
                right = left + 1
                continue
            maxprofit = max(maxprofit, profit)
            right = left + 2 if right == len(prices) else right + 1
            left = left + 1 if right == len(prices) else left
        return maxprofit


# input = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9]
# solution = Solution()
# print(solution.maxProfit(input))

# @lc code=end
