class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]
        memo = [nums[0], max(nums[0], nums[1])]
        for i in range(2, length):
            memo.append(max(memo[i - 2] + nums[i], memo[i - 1]))
        return memo[length - 1]
        
        