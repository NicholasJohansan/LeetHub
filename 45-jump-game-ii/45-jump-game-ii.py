class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        max_reach = [nums[0]] + [float('-inf')] * (len(nums) - 1)
        for i in range(1, len(nums)):
            max_reach[i] = max(max_reach[i - 1], nums[i] + i)
            
        jumps = 0
        furthest_reach = 0
        for i in range(len(nums)):
            if i == furthest_reach:
                jumps += 1
                if max_reach[i] >= len(nums) - 1:
                    break
                furthest_reach = max_reach[i]
            
        return jumps
            