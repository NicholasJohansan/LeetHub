class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0
        while l < r:
            length = r - l
            l_height = height[l]
            r_height = height[r]
            area = min(l_height, r_height) * length
            max_area = max(area, max_area)
            if l_height < r_height:
                l += 1
            else:
                r -= 1
        return max_area
        