# https://leetcode.com/problems/set-matrix-zeroes/
from functools import reduce
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        first_element_zero = matrix[0][0] == 0
        first_row_has_zero = 0 in [matrix[0][i] for i in range(1, n)]
        first_column_has_zero = 0 in [matrix[i][0] for i in range(1, m)]

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
        if first_element_zero:
            for i in range(1, m):
                matrix[i][0] = 0
            for j in range(1, n):
                matrix[0][j] = 0
        if first_row_has_zero:
            for j in range(0, n):
                matrix[0][j] = 0
        if first_column_has_zero:
            for i in range(0, m):
                matrix[i][0] = 0
