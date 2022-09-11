class Solution:
    def isHappy(self, n: int) -> bool:
        encountered = set()
        while n != 1:
            if n in encountered:
                return False
            encountered.add(n)
            new_n = 0
            for num in str(n):
                new_n += int(num) ** 2
            n = new_n
        return True