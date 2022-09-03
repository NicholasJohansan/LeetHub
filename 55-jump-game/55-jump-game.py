class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        if length == 1:
            return True
        max_steps_left = [nums[0]] + [float("-inf")] * (length - 1)
        for i in range(1, length):
            max_steps_left[i] = max(max_steps_left[i - 1], nums[i - 1]) - 1
            if max_steps_left[i] < 0:
                return False
        return max_steps_left[length - 1] >= 0
            