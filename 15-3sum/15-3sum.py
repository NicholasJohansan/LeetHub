class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for i in range(len(nums) - 2):
            if i - 1 >= 0 and nums[i] == nums[i - 1]: continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                nums_sum = nums[i] + nums[l] + nums[r]
                if nums_sum > 0:
                    r -= 1
                elif nums_sum < 0:
                    l += 1
                else:
                    triplets.append([nums[i], nums[l], nums[r]])
                    while l + 1 < r and nums[l] == nums[l + 1]:
                        l += 1
                    while r - 1 > l and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return triplets
                    
        