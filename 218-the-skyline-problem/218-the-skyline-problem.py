class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        points = []
        for left, right, height in buildings:
            points.append((left, -height))
            points.append((right, height))
        points.sort()

        skyline = []
        heights = [0]
        prev_max_height = 0
        for x, height in points:
            if height < 0:
                heights.append(abs(height))
            else:
                heights.remove(height)
            max_height = max(heights)
            if prev_max_height != max_height:
                skyline.append([x, max_height])
                prev_max_height = max_height
        return skyline