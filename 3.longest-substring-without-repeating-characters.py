#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

from typing import * # type: ignore
from collections import defaultdict

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        present = defaultdict(bool)
        left = 0
        right = 0
        maxLen = 0
        while right < len(s):
            notPresent = present[s[right]] == False
            if notPresent:
                present[s[right]] = True
                right = right + 1
                maxLen = max(maxLen, right - left)
            else:
                maxLen = max(maxLen, right - left)
                present = defaultdict(bool)
                left = left + 1
                right = left
        return maxLen

# input = "abcabcbb"
# solution = Solution()
# print(solution.lengthOfLongestSubstring(input))

# @lc code=end

