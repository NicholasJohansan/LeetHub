class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i in range(len(nums)):
            num = nums[i]
            if target - num in indices:
                return [indices[target - num], i]
            indices[nums[i]] = i
        return -1