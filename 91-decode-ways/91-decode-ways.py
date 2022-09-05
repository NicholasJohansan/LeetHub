class Solution:
    def numDecodings(self, s: str) -> int:
        total_number = [0 for i in range(len(s) + 1)]
        total_number[0] = 1
        for i in range(1, len(s) + 1):
            if s[i - 1] != "0":
                total_number[i] = total_number[i - 1]
            if i > 1:
                prev_number = int(s[i - 2] + s[i - 1])
                if prev_number > 9 and prev_number < 27:
                    total_number[i] += total_number[i - 2]
                
        return total_number[len(s)]