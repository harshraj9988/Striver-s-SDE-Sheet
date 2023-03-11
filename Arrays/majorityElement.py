# https://leetcode.com/problems/majority-element/
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele, cnt = nums[0], 0
        for num in nums:
            if num == ele:
                cnt += 1
            elif cnt == 0:
                ele, cnt = num, 1
            else:
                cnt -= 1
        return ele
