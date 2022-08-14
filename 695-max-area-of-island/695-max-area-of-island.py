class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.visited = set()
        max_area = 0
        self.rows = len(grid)
        self.cols = len(grid[0])
        for row in range(self.rows):
            for col in range(self.cols):
                if (row, col) not in self.visited:
                    self.visited.add((row, col))
                    if grid[row][col] == 1:
                        area = self.calculate_area(row, col, grid)
                        if area > max_area:
                            max_area = area
                
        return max_area
        
        
    def calculate_area(self, row: int, col: int, grid: List[List[int]]):
        area = 1
        possible_paths = [
            (row + 1, col    ),
            (row - 1, col    ),
            (row    , col + 1),
            (row    , col - 1)
        ]
        for n_row, n_col in possible_paths:
            if not ((n_row >= 0 and n_row < self.rows) and (n_col >= 0 and n_col < self.cols)):
                continue
            
            if grid[n_row][n_col] != 1 or (n_row, n_col) in self.visited:
                continue
            
            self.visited.add((n_row, n_col))
            area += self.calculate_area(n_row, n_col, grid)
        return area