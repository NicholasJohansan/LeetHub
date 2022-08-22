class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        index = 0
        last = matrix[0][0]
        current = 0
        row = 0
        for i in range(1, len(matrix)):
            current = matrix[i][0]
            if target < current and target >= last:
                row = i - 1
                break
            last = current
            
        if target >= matrix[-1][0]:
            row = len(matrix) - 1
        
        nums = matrix[row]
        
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            num = nums[mid]
            if target == num:
                return True
            elif target < num:
                r = mid - 1
            else:
                l = mid + 1
        return False
        