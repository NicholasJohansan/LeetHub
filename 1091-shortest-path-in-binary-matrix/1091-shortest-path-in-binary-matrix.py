class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue = [(0, 0)]
        n = len(grid)
        path_length = 0
        visited = set()
        while queue:
            path_length += 1
            length = len(queue)
            for i in range(length):
                row, col = queue.pop(0)
                if row < 0 or row >= n or col < 0 or col >= n:
                    continue
                if grid[row][col] == 1:
                    continue
                if row == n - 1 and col == n -1:
                    return path_length
                if (row, col) in visited:
                    continue
                visited.add((row, col))
                queue.append((row + 1, col + 1))
                queue.append((row + 1, col - 1))
                queue.append((row + 1, col    ))
                queue.append((row    , col + 1))
                queue.append((row    , col - 1))
                queue.append((row - 1, col + 1))
                queue.append((row - 1, col - 1))
                queue.append((row - 1, col    ))
        return -1
                