class Solution:
    def reverseVowels(self, s: str) -> str:
        string = list(s)
        l = 0
        r = len(s) - 1
        while l <= r:
            while l < len(s) and string[l].lower() not in "aeiou":
                l += 1
            if l == len(s) or l > r:
                break
            while r > 0 and string[r].lower() not in "aeiou":
                r -= 1
            if r < 0 or r < l:
                break
            string[l], string[r] = string[r], string[l]
            l += 1
            r -= 1
        return "".join(string)
                