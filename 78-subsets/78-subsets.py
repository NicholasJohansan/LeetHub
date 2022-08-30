class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.length = len(nums)
        self.sets = [[]]
        for i in range(self.length):
            self.find_subset(nums, i, [])
        return self.sets
    
    def find_subset(self, nums, start, subset):
        subset = list(subset)
        subset.append(nums[start])
        self.sets.append(subset)
        for i in range(start + 1, self.length):
            self.find_subset(nums, i, subset)
        
    
    
        