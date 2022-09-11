class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return len(points)
        max_pts = 2
        for point1 in points:
            x1, y1 = point1
            gradients = {}
            for point2 in points:
                if point2 == point1:
                    continue
                x2, y2 = point2
                dy = y2 - y1
                dx = x2 - x1
                if dx == 0:
                    gradients["inf"] = gradients.get("inf", 0) + 1
                else:
                    gradient = str(dy/dx)
                    gradients[gradient] = gradients.get(gradient, 0) + 1
            curr_max_pts = sorted(gradients.values(), reverse=True)[0]
            max_pts = max(max_pts, curr_max_pts + 1)
        return max_pts
            