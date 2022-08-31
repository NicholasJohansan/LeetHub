class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.permutations = []
        self.nums = nums
        self.nums_length = len(nums)
        self.permute([], self.nums)
        return self.permutations

    def permute(self, permutation: List[int], remainding: List[int]) -> None:
        if len(permutation) == self.nums_length:
            if permutation not in self.permutations:
                self.permutations.append(permutation)
        else:
            for i in range(len(remainding)):
                num = remainding[i]
                new_remainding = remainding[:i] + remainding[i+1:]
                self.permute(permutation + [num], new_remainding)