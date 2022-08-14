class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.color = image[sr][sc]
        if self.color != color:
            self.fill_color(image, sr, sc, color)
        return image
        
    def fill_color(self, image: List[List[int]], row: int, col: int, new_color: int):
        rows = len(image)
        cols = len(image[0])
        
        if not ((row >= 0 and row < rows) and (col >= 0 and col < cols)):
            return
        
        if image[row][col] != self.color:
            return
        
        image[row][col] = new_color
        
        self.fill_color(image, row + 1, col    , new_color)
        self.fill_color(image, row - 1, col    , new_color)
        self.fill_color(image, row    , col + 1, new_color)
        self.fill_color(image, row    , col - 1, new_color)
        