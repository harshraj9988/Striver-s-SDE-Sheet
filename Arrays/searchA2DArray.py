from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        start, end = 0, m * n - 1
        while start <= end:
            mid = start + (end - start) // 2
            x, y = mid // n, mid % n
            if matrix[x][y] == target:
                return True
            if matrix[x][y] < target:
                start = mid + 1
            else:
                end = mid - 1
        return False
