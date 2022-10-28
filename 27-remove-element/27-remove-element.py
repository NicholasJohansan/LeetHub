class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l = 0
        r = 0
        while r < len(nums):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
            r += 1
        for _ in range(r - l):
            nums.pop()