class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pointer = 0
        for i in range(len(nums)):
            num = nums[i]
            if num != 0:
                nums[pointer] = num
                pointer += 1
        while pointer < len(nums):
            nums[pointer] = 0
            pointer += 1