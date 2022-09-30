class Solution:
    def concatenatedBinary(self, n: int) -> int:
        if n == 1:
            return 1
        bin_rep = ""
        for num in range(1, n + 1):
            bin_num = bin(num)[2:]
            bin_rep += bin_num
        return int("0b" + bin_rep, 2) % (10**9 + 7)