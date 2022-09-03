class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]
        elif length == 2:
            return max(nums[0], nums[1])
        
        # first, 0th to (length - 2)th
        memo1 = [nums[0], max(nums[0], nums[1])]
        for i in range(2, length - 1):
            memo1.append(max(memo1[i - 2] + nums[i], memo1[i - 1]))
        first = memo1[length - 2]
        
        # second, 1st to (length - 1)th
        second = -1
        if length >= 3:
            memo2 = [nums[1], max(nums[1], nums[2])]
            for i in range(2, length - 1):
                memo2.append(max(memo2[i - 2] + nums[i + 1], memo2[i - 1]))
            second = memo2[length - 2]
        else:
            second = nums[1]
        
        return max(first, second)