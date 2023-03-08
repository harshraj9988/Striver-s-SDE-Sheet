# https://leetcode.com/problems/maximum-subarray/
# Kadane's Algo
import sys
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -sys.maxsize
        curr_sum = 0

        for num in nums:
            if curr_sum + num < num:
                curr_sum = num
            else:
                curr_sum += num
            max_sum = max(max_sum, curr_sum)

        return max_sum
