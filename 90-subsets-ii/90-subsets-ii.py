class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.length = len(nums)
        self.sets = [[]]
        self.sets_counts = [{}]
        for i in range(self.length):
            self.find_subset(nums, i, [])
        return self.sets
    
    def find_subset(self, nums, start, subset):
        subset = list(subset)
        subset.append(nums[start])
        subset_count = self.make_set_count(subset)
        if subset_count not in self.sets_counts:
            self.sets_counts.append(subset_count)
            self.sets.append(subset)
        for i in range(start + 1, self.length):
            self.find_subset(nums, i, subset)
            
    def make_set_count(self, subset):
        set_count = {}
        for num in subset:
            set_count[num] = set_count.get(num, 0) + 1
        return set_count
        