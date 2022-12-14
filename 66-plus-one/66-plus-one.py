class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for pos in range(len(digits) - 1, -1, -1):
            if digits[pos] + 1 > 9:
                digits[pos] = 0
            else:
                digits[pos] += 1
                break
        if digits[0] == 0:
            digits = [1] + digits
        return digits
            