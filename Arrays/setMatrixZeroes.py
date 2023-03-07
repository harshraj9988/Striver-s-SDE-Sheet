# https://leetcode.com/problems/set-matrix-zeroes/
from functools import reduce
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n, first_col = len(matrix), len(matrix[0]), True

        for i in range(m):
            if matrix[i][0] == 0:
                first_col = False
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0

        for i in range(m-1, -1, -1):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if not first_col:
                matrix[i][0] = 0
