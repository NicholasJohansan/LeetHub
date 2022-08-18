class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.permutations = []
        self.nums = nums
        self.nums_length = len(nums)
        self.make_permutations([], self.nums)
        return self.permutations

    def make_permutations(self, permutation: List[int], remainding: List[int]) -> None:
        if len(permutation) == self.nums_length:
            self.permutations.append(permutation)
        else:
            for i in range(len(remainding)):
                num = remainding[i]
                self.make_permutations(permutation + [num], [n for n in remainding if n != num])
                
            
        
        