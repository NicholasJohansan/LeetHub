class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) < 2:
            return ""
        string = list(palindrome)
        for i in range(len(palindrome) // 2):
            if palindrome[i] != "a":
                string[i] = "a"
                return "".join(string)
        string[len(palindrome) - 1] = "b"
        return "".join(string)