class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = 0
        prev = None
        while r < len(nums):
            if nums[r] != prev:
                prev = nums[r]
                nums[l] = nums[r]
                l += 1
            r += 1
        while len(nums) > l:
            nums.pop()