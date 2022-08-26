class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')
        num_sum = 0
        left = 0
        for right in range(len(nums)):
            num_sum += nums[right]
            while num_sum >= target:
                min_length = min(min_length, right - left + 1)
                num_sum -= nums[left]
                left += 1
        return 0 if min_length == float('inf') else min_length
        