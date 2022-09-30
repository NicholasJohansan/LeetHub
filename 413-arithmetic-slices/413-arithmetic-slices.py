class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        arithmetic_slices = [0 for i in range(len(nums))]
        total = 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                arithmetic_slices[i] = arithmetic_slices[i - 1] + 1
            else:
                arithmetic_slices[i] = 0
            total += arithmetic_slices[i]
        return total