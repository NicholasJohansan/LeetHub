class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.visited = set()
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) not in self.visited and grid[i][j] == "1":
                    self.traverse(grid, i, j)
                    islands += 1
        return islands
                
                
    def traverse(self, grid: List[List[str]], i: int, j: int):
        if (i < 0 or i >= len(grid)) or (j < 0 or j >= len(grid[i])):
            return
        if (i, j) in self.visited:
            return
        if grid[i][j] == "0":
            return
        self.visited.add((i, j))
        self.traverse(grid, i + 1, j    )
        self.traverse(grid, i - 1, j    )
        self.traverse(grid, i    , j + 1)
        self.traverse(grid, i    , j - 1)