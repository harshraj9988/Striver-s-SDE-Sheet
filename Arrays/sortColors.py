# https://leetcode.com/problems/sort-colors/
# Dutch Partitioning problem
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        red, white, blue = 0, 0, len(nums) - 1

        while white < blue:
            if nums[white] == 0:    # red at whites pos, we swap them
                nums[white], nums[red] = nums[red], nums[white]
                white += 1
                red += 1
            elif nums[white] == 1:  # white at whites pos, do nothing
                white += 1
            else:                   # blue at whites pos, we swap them
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
