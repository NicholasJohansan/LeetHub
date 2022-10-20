class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = ["" for _ in range(numRows)]
        row = 0
        is_up = 0
        for char in s:
            rows[row] += char
            if is_up:
                row -= 1
                if row < 1:
                    row = 0 if numRows > 2 else 1
                    is_up = 0
            elif not is_up:
                row += 1
                if row > numRows - 1:
                    row = numRows - 2
                    is_up = 1
        print(rows)
        return "".join(rows)
                
                
            