#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#
from operator import index
from typing import *  # type: ignore
from collections import defaultdict

# @lc code=start


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.rowValidator(board) and self.columnValidator(board) and self.squareValidator(board)

    def rowValidator(self, board: List[List[str]]) -> bool:
        for row in board:
            dict = defaultdict(int)
            for element in row:
                if element != ".":
                    dict[element] = dict[element] + 1
            for value in dict.values():
                if value > 1:
                    return False
        return True

    def columnValidator(self, board: List[List[str]]) -> bool:
        for indexX in range(9):
            dict = defaultdict(int)
            for indexY in range(9):
                element = board[indexY][indexX]
                if element != ".":
                    dict[element] = dict[element] + 1
            for value in dict.values():
                if value > 1:
                    return False
        return True

    def squareValidator(self, board: List[List[str]]) -> bool:
        for indexX in range(0, 9, 3):
            for indexY in range(0, 9, 3):
                dict = defaultdict(int)
                accumulated = []
                for count in range(3):
                    accumulated.extend(
                        board[indexX + count][indexY: indexY + 3])
                for item in accumulated:
                    if item != ".":
                        dict[item] = dict[item] + 1
                for value in dict.values():
                    if value > 1:
                        return False
        return True


# solution = Solution()
# board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
#                                                                                                                                                                                                       ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

# print(solution.isValidSudoku(board))

# @lc code=end
