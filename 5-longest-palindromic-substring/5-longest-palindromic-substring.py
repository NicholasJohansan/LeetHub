class Solution:
    def longestPalindrome(self, s: str) -> str:
        is_palindrome = [[False for i in range(len(s))] for i in range(len(s))]
        max_length = float("-inf")
        l = float("-inf")
        r = float("-inf")
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if i == j:
                    is_palindrome[i][j] = True
                elif s[i] == s[j]:
                    if j - i == 1:
                        is_palindrome[i][j] = True
                    else:
                        is_palindrome[i][j] = is_palindrome[i+1][j-1]
                if is_palindrome[i][j] and j - i >= max_length:
                    max_length = j - i
                    l = i
                    r = j
        return s[l:r+1]