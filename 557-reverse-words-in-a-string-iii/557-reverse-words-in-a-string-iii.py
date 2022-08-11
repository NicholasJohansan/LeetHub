class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        l = 0
        prev = " "
        last_index = len(s) - 1
        for i in range(len(s)):
            current = s[i]
            if prev == " ":
                l = i
            if current == " ":
                self.reverse(s, l, i - 1)
            elif i == last_index and prev != " ":
                self.reverse(s, l, i)
            prev = current
        return "".join(s)
            
        
    def reverse(self, s: str, l: int, r: int):
        while l < r:
            left = s[l]
            right = s[r]
            s[l] = right
            s[r] = left
            l += 1
            r -= 1