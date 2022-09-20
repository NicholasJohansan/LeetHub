class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        if nums1 == nums2:
            return len(nums1)
        repeated_length = [[0 for i in range(len(nums2) + 1)] for i in range(len(nums1) + 1)]
        max_length = 0
        for i in range(1, len(nums1) + 1):
            char1 = nums1[i - 1]
            for j in range(1, len(nums2) + 1):
                char2 = nums2[j - 1]
                if char1 == char2:
                    repeated_length[i][j] = repeated_length[i - 1][j - 1] + 1
                    max_length = max(max_length, repeated_length[i][j])
        return max_length