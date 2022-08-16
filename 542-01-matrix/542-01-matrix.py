class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        dist = [[float('inf') for _ in range(n)] for _ in range(m)]
        
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    dist[row][col] = 0
                else:
                    if row > 0:
                        dist[row][col] = min(dist[row - 1][col] + 1, dist[row][col])
                    if col > 0:
                        dist[row][col] = min(dist[row][col - 1] + 1, dist[row][col])
        
        for row in range(m):
            row = m - 1 - row
            for col in range(n):
                col = n - 1 - col
                if row < m - 1:
                    dist[row][col] = min(dist[row + 1][col] + 1, dist[row][col])
                if col < n - 1:
                    dist[row][col] = min(dist[row][col + 1] + 1, dist[row][col])
        
        return dist