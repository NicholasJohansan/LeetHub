class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sorted_list = []
        l = 0
        r = len(nums) - 1;
        for _ in range(len(nums) - 1, -1, -1):
            l_num = abs(nums[l])
            r_num = (nums[r])
            if l_num > r_num:
                sorted_list.insert(0, l_num ** 2)
                l += 1
            else:
                sorted_list.insert(0, r_num ** 2)
                r -= 1
        return sorted_list