class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        paths = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        if obstacleGrid[0][0] == 1:
            return 0
        paths[0][0] = 1
        
        for row in range(1, len(obstacleGrid)):
            if obstacleGrid[row][0] == 1:
                break
            paths[row][0] = paths[row - 1][0]
            
        for col in range(1, len(obstacleGrid[0])):
            if obstacleGrid[0][col] == 1:
                break
            paths[0][col] = paths[0][col - 1]
            
        for row in range(1, len(obstacleGrid)):
            for col in range(1, len(obstacleGrid[row])):
                if obstacleGrid[row][col] == 1:
                    continue
                paths[row][col] += paths[row - 1][col] + paths[row][col - 1]
        
        return paths[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1]