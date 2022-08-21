class Solution:
    def reverseBits(self, n: int) -> int:
        bits = list(bin(n))
        if len(bits) != 34:
            bits = ["0", "b"] + (["0"] * (34 - len(bits))) + bits[2:]
        l = 2
        r = len(bits) - 1
        while l < r:
            temp = bits[l]
            bits[l] = bits[r]
            bits[r] = temp
            r -= 1
            l += 1
        return int("".join(bits), 2)