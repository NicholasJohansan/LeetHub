class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        abs_diffs = [(num, abs(num - x)) for num in arr]
        abs_diffs.sort(key=lambda diff: diff[1])
        nums = [diff[0] for diff in abs_diffs[:k]]
        return sorted(nums)