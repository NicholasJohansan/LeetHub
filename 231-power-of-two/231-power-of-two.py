class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        bits = bin(n)[2:]
        return bits[0] == "1" and all([bit == "0" for bit in bits[1:]])