class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        length1 = len(word1)
        length2 = len(word2)
        min_ops = [[float('inf') for i in range(length2 + 1)] for i in range(length1 + 1)]
        for i in range(length1 + 1):
            min_ops[i][0] = i
        for i in range(length2 + 1):
            min_ops[0][i] = i
        for i in range(1, length1 + 1):
            for j in range(1, length2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    min_ops[i][j] = min_ops[i - 1][j - 1]
                else:
                    min_ops[i][j] = min(
                        min_ops[i - 1][j - 1], # replace
                        min_ops[i - 1][j], # delete
                        min_ops[i][j - 1] # insert
                    ) + 1
        return min_ops[length1][length2]