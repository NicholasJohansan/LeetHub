class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        lcs = self.get_lcs(word1, word2)
        return len(word1) + len(word2) - (lcs * 2)
        
    def get_lcs(self, text1, text2):
        n = len(text1)
        m = len(text2)
        lcs = [[0 for i in range(m + 1)] for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    lcs[i][j] = lcs[i - 1][j - 1] + 1
                else:
                    lcs[i][j] = max(lcs[i][j - 1], lcs[i - 1][j])
        return lcs[n][m]