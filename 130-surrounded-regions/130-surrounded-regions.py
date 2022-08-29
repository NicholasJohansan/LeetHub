class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        
        self.stack = []
        for i in range(rows):
            self.checkO(board, i, 0)
            self.checkO(board, i, cols - 1)
        for i in range(cols):
            self.checkO(board, 0, i)
            self.checkO(board, rows - 1, i)
            
        visited = set()
        while self.stack:
            row, col = self.stack.pop()
            if (row, col) in visited:
                continue
            visited.add((row, col))
            for row, col in [
                (row + 1, col    ),
                (row - 1, col    ),
                (row    , col + 1),
                (row    , col - 1)
            ]:
                
                if row < 0 or row >= rows or col < 0 or col >= cols:
                    continue
                if board[row][col] == "O":
                    board[row][col] = "STAY O"
                    self.stack.append((row, col))
            
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "STAY O":
                    board[i][j] = "O"
    
    def checkO(self, board, row, col):
        if board[row][col] == "O":
            board[row][col] = "STAY O"
            self.stack.append((row, col))
            
        
        