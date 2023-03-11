# https://leetcode.com/problems/majority-element-ii/
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = dict()
        ans = list()
        n = len(nums) // 3
        for num in nums:
            count[num] = count.get(num, 0) + 1

        for key, val in count:
            if val > n:
                ans.append(key)

        return ans
