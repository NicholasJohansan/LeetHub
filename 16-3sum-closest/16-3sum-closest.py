class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                nums_sum = nums[i] + nums[l] + nums[r]
                if abs(target - nums_sum) < abs(target - closest_sum):
                    closest_sum = nums_sum
                if nums_sum > target:
                    r -= 1
                else:
                    l += 1
        return closest_sum
                    
        