class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        max_scores = [0 for _ in range(len(multipliers) + 1)]
        
        for ops in range(len(multipliers) - 1, -1, -1):
            multiplier = multipliers[ops]
            orig_max_scores = max_scores[:]
            
            for start in range(ops, -1, -1):
                max_scores[start] = max(
                    multiplier * nums[start] + orig_max_scores[start + 1],
                    multiplier * nums[len(nums) - 1 - ops + start] + orig_max_scores[start]
                )
                
        return max_scores[0]