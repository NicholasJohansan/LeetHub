class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.word = word
        for i in range(len(board)):
            for j in range(len(board[i])):
                if self.find_word(board, i, j, set(), ""):
                    return True
        return False
    
    def find_word(self, board, i, j, visited, found):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]):
            return False
        if (i, j) in visited:
            return False
        letter = board[i][j]
        index = len(found)
        if index < len(self.word):
            if self.word[index] == letter:
                found += letter
                if found == self.word:
                    return True
                visited.add((i, j))
                if any([
                    self.find_word(board, row, col, visited, found)
                    for row, col in [
                        (i + 1, j    ),
                        (i - 1, j    ),
                        (i    , j + 1),
                        (i    , j - 1)
                    ]
                ]):
                    return True
                else:
                    visited.remove((i, j))
                    return False
            else:
                return False
        else:
            return self.word == found
        
        
        