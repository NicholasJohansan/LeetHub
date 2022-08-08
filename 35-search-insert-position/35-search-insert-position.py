class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            num = nums[mid]
            if target == num:
                return mid
            elif target > num:
                l = mid + 1
            else:
                r = mid - 1
        return l
        