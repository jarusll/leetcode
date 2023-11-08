#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

from typing import *  # type: ignore

# @lc code=start


class Solution:
    def trap(self, height: List[int]) -> int:
        minmax = {}
        for current in range(1, len(height) - 1, 1):
            leftIndex = current - 1
            rightIndex = current + 1
            maxleft = height[current]
            maxright = height[current]
            if height[current] < height[leftIndex]:
                maxleft = height[leftIndex]
            if height[current] < height[rightIndex]:
                maxright = height[rightIndex]



input = [4, 2, 3]
solution = Solution()
print(solution.trap(input))

# @lc code=end
