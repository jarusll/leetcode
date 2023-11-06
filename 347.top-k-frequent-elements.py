#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
from collections import defaultdict
import random
from typing import Tuple, List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:  # type: ignore
        heap = []
        occurence = defaultdict(int)
        maxOccurence = []
        for item in nums:
            occurence[item] += 1
        for key, value in occurence.items():
            heap.append([key, value])
        for index in range((len(heap) - 1) // 2, -1, -1):
            self.heapifyDown(heap, index)
        for i in range(k):
            maxOccurence.append(heap.pop(0))
            for index in range((len(heap) - 1) // 2, -1, -1):
                self.heapifyDown(heap, index)
        return list(map(lambda x: x[0], maxOccurence))

    def heapifyDown(self, heap: List[Tuple[int, int]], index: int) -> None:  # type: ignore
        maximum = index
        left = 2 * index + 1
        right = 2 * index + 2
        if left < len(heap) and heap[maximum][1] < heap[left][1]:
            maximum = left
        if right < len(heap) and heap[maximum][1] < heap[right][1]:
            maximum = right
        if maximum != index:
            heap[index], heap[maximum] = heap[maximum], heap[index]
            self.heapifyDown(heap, maximum)

# solution = Solution()
# randomizedList = list([random.randrange(0, 10, 3) for x in range(100)])
# print(randomizedList)
# print(solution.topKFrequent(randomizedList, 2))
# @lc code=end
