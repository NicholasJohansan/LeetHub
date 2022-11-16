from collections import deque

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        sums = [[float('inf') for _ in range(len(grid[i]))] for i in range(len(grid))]
        sums[0][0] = grid[0][0]
        
        for row in range(1, len(grid)):
            sums[row][0] = sums[row - 1][0] + grid[row][0]
            
        for col in range(1, len(grid[0])):
            sums[0][col] = sums[0][col - 1] + grid[0][col]
            
        for row in range(1, len(grid)):
            for col in range(1, len(grid[row])):
                sums[row][col] = min(sums[row - 1][col], sums[row][col - 1]) + grid[row][col]
        
        return sums[len(grid) - 1][len(grid[0]) - 1]