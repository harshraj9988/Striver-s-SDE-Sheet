# https://leetcode.com/problems/pascals-triangle/
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        final_list = list()
        for i in range(numRows):
            temp_list = list()
            for j in range(numRows):
                if j == 0 or j == numRows - 1:
                    temp_list.append(1)
                else:
                    temp_list.append(final_list[i - 1][j - 1] + final_list[i - 1][j])
            final_list.append(temp_list)
        return final_list
