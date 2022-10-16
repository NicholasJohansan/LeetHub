class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1
        difficulty = [([0] + [float('inf')] * len(jobDifficulty)) for _ in range(d+1)]
        for i in range(1, d+1):
            for j in range(1, len(jobDifficulty)+1):
                currentDifficulty = 0
                for k in range(j, i-1, -1):
                    currentDifficulty = max(currentDifficulty, jobDifficulty[k - 1])
                    difficulty[i][j] = min(difficulty[i][j], currentDifficulty + difficulty[i-1][k-1])
        return difficulty[d][len(jobDifficulty)]
                    