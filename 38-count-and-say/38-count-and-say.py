class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        prev = self.countAndSay(n - 1)
        new = ""
        count = 1
        num = prev[0]
        for i in range(1, len(prev)):
            if prev[i] != num:
                new += str(count) + str(num)
                num = prev[i]
                count = 1
            else:
                count += 1
        new += str(count) + str(num)
        return new
            
        