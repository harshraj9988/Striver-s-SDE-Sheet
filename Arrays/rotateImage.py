# https://leetcode.com/problems/rotate-image/
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])

        for i in range(m - 1, -1, -1):  # transpose along [/]
            for j in range(m - 1 - i):
                matrix[i][j], matrix[-1 - j][-1 - i] = matrix[-1 - j][-1 - i], matrix[i][j]

        for i in range(m // 2):  # reverse the matrix [=] row wise
            matrix[i], matrix[-i - 1] = matrix[-i - 1], matrix[i]
