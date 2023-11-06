#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

from typing import *

# @lc code=start


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximumArea = 0
        left = 0
        right = len(height) - 1
        while left < right:
            area = (right - left) * min(height[left], height[right])
            maximumArea = max(area, maximumArea)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            continue
        return maximumArea


# input = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# solution = Solution()
# print(solution.maxArea(input))


# @lc code=end
