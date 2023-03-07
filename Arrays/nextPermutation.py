# https://leetcode.com/problems/next-permutation/
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind = ind1 = n = len(nums) - 1
        ind -= 1

        while ind >= 0 and nums[ind] >= nums[ind+1]:
            ind -= 1

        if ind == -1:
            nums.reverse()
            return

        while ind1 > ind and nums[ind1] <= nums[ind]:
            ind1 -= 1

        nums[ind], nums[ind1] = nums[ind1], nums[ind]

        ind += 1
        while ind < n:
            nums[ind], nums[n] = nums[n], nums[ind]
            ind += 1
            n -= 1
