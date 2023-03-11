# https://leetcode.com/problems/powx-n/

class Solution:
    def pow_recursion(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        temp = self.pow(x, n // 2)
        if n % 2 == 0:
            return temp * temp
        else:
            return x * temp * temp

    def pow_iteration(self, x: float, n: int) -> float:
        ans = 1.0
        while n > 0:
            if n % 2 == 1:
                ans = ans * x
                n -= 1
            else:
                x *= x
                n /= 2
        return ans

    def myPow(self, x: float, n: int) -> float:
        neg = True if n < 0 else False
        ans = self.pow_iteration(x, abs(n))
        if neg:
            return 1 / ans
        return ans
