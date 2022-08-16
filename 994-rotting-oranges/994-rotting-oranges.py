class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        oranges_count = 0
        rotten_oranges = set()
        
        for row in range(m):
            for col in range(n):
                row_status = grid[row][col]
                if row_status != 0:
                    oranges_count += 1
                if row_status == 2:
                    rotten_oranges.add((row, col))
        
        minutes = 0
        while oranges_count != len(rotten_oranges):
            orig_rotten_count = len(rotten_oranges)
            minutes += 1
            
            for row, col in rotten_oranges.copy():
                adjacent = [
                    (row + 1, col    ),
                    (row - 1, col    ),
                    (row    , col + 1),
                    (row    , col - 1)
                ]
                for row, col in adjacent:
                    if not (row >= 0 and row < m and col >= 0 and col < n):
                        continue
                    cell_status = grid[row][col]
                    if cell_status != 1:
                        continue
                    grid[row][col] = 2
                    rotten_oranges.add((row, col))
            
            if len(rotten_oranges) == orig_rotten_count:
                return -1
        return minutes
                