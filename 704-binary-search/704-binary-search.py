class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        left = 0
        right = length - 1
        while left <= right:
            mid = (left + right) // 2
            num = nums[mid]
            if target == num:
                return mid
            elif target > num:
                left = mid + 1
            else:
                right = mid - 1
        return -1