class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis_length = [1 for i in range(len(nums))]
        for i in range(len(nums)):
            num = nums[i]
            prev_lis_length = [lis_length[i]]
            for j in range(i):
                prev_num = nums[j]
                if prev_num < num:
                    prev_lis_length.append(lis_length[j] + 1)
            lis_length[i] = max(prev_lis_length)
        return max(lis_length)
                    
        