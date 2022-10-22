class Solution:
    def reverse(self, x: int) -> int:
        multiplier = -1 if x < 0 else 1
        num = abs(x)
        res = 0
        while num:
            digit = num % 10
            res *= 10
            res += digit
            num //= 10
        res *= multiplier
        if res > 2 ** 31 - 1 or res < -2 ** 31:
            return 0
        return res
            