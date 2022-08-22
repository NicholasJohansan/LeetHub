class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        k = l
        if target >= nums[k] and target <= nums[-1]:
            l = k
            r = len(nums) - 1
        else:
            l = 0
            r = k
        
        while l <= r:
            mid = (l + r) // 2
            num = nums[mid]
            if num == target:
                return mid
            elif target < num:
                r = mid - 1
            else:
                l = mid + 1
        return -1