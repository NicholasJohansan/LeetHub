class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        first = float('inf')
        second = float('inf')
        for num in nums:
            if num < first:
                first = num
            if num > first:
                second = min(num, second)
            if num > second:
                return True
        return False