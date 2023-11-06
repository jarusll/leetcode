#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

from typing import *  # type:ignore

# @lc code=start


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sticky = 0
        left = sticky + 1
        right = len(nums) - 1
        result = {}
        while sticky < len(nums) - 2:
            if left >= right:
                sticky += 1
                left = sticky + 1
                right = len(nums) - 1
                continue
            if right <= left:
                sticky += 1
                left = sticky + 1
                right = len(nums) - 1
                continue
            sum = nums[sticky] + nums[left] + nums[right]
            if sum == 0:
                indexes = [nums[sticky], nums[left], nums[right]]
                result[str(indexes)] = indexes
                left += 1
                continue
            if sum < 0:
                left += 1
                continue
            if sum > 0:
                right -= 1
                continue
        return list(result.values())


# solution = Solution()
# input = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
# print('sorted', input.sort())
# print(input)
# print(solution.threeSum(input))
# @lc code=end
