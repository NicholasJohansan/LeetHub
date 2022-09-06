class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        lis_length = [[1, 1] for i in range(len(nums))]
        for i in range(len(nums)):
            num = nums[i]
            for j in range(i):
                prev_num = nums[j]
                if prev_num < num:
                    length, count = lis_length[i]
                    prev_length, prev_count = lis_length[j]
                    if prev_length + 1 == length:
                        lis_length[i][1] += prev_count
                    elif prev_length + 1 > length:
                        lis_length[i][1] = prev_count
                        lis_length[i][0] = prev_length + 1
        longest_length = max([l for l, _ in lis_length])
        total_count = 0
        for length, count in lis_length:
            if length == longest_length:
                total_count += count
        return total_count
                    
        