from math import ceil
class Solution:
    def integerBreak(self, n: int) -> int:
        
        if n == 2:
            return 1
        elif n == 3:
            return 2
        
        left = n
        product = 1
        while left > 0:
            if left > 2 and left % 3 == 0:
                product *= 3
                left -= 3
            else:
                product *= 2
                left -= 2
        return product