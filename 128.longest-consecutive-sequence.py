#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start

from typing import *  # type: ignore
from collections import defaultdict


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited = defaultdict(bool)
        ranges = defaultdict(list)
        maximum = 0
        for item in nums:
            if visited[item]:
                continue
            visited[item] = True
            l, r = item, item
            # left side check
            if visited[l - 1]:
                l = ranges[r - 1][0]
            # right side check
            if visited[r + 1]:
                r = ranges[r + 1][1]
            ranges[l] = [l, r]
            ranges[r] = [l, r]
            maximum = max(maximum, r - l + 1)
        return maximum


# solution = Solution()
# print(solution.longestConsecutive([4, 2, 2, -4, 0, -2, 4, -3, -4, -
#       4, -5, 1, 4, -9, 5, 0, 6, -8, -1, -3, 6, 5, -8, -1, -5, -1, 2, -9, 1]))

# @lc code=end
