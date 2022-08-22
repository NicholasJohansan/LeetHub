class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        first = -1
        while l <= r:
            mid = (l + r) // 2
            num = nums[mid]
            if target == num:
                first = mid
                r = mid - 1
            elif target < num:
                r = mid - 1
            else:
                l = mid + 1
                
        l = 0
        r = len(nums) - 1
        last = -1
        while l <= r:
            mid = (l + r) // 2
            num = nums[mid]
            if target == num:
                last = mid
                l = mid + 1
            elif target < num:
                r = mid - 1
            else:
                l = mid + 1
                
        
        return [first, last]