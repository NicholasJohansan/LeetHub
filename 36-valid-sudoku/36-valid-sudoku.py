class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(len(board)):
            row = board[r]
            for c in range(len(row)):
                num = row[c]
                if num == ".":
                    continue
                
                # check row
                for i in range(len(row)):
                    if i == c:
                        continue
                    if row[i] == num:
                        return False
                
                # check col
                for i in range(len(board)):
                    if i == r:
                        continue
                    if board[i][c] == num:
                        return False
                    
                # check box
                box_x = c // 3
                box_y = r // 3
                for r2 in range(box_y * 3, (box_y * 3) + 3):
                    for c2 in range(box_x * 3, (box_x * 3) + 3):
                        if r2 == r and c2 == c:
                            continue
                        if board[r2][c2] == num:
                            return False
        return True