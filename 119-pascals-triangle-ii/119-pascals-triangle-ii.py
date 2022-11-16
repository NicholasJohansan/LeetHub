class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        numRows = rowIndex + 1
        triangle = [[1 for _ in range(n + 1)] for n in range(numRows)]
        for i in range(2, numRows):
            for j in range(1, len(triangle[i]) - 1):
                triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        return triangle[rowIndex]
        