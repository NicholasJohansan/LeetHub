class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = candidates
        self.target = target
        self.combinations = []
        self.find_combination([], 0, 0)
        return self.combinations
        
    def find_combination(self, combination, combination_sum, index):
        if index == len(self.candidates):
            if combination_sum == self.target:
                self.combinations.append(combination)
            return
        
        num = self.candidates[index]
        if combination_sum + num <= self.target:
            self.find_combination(combination + [num], combination_sum + num, index)
        
        self.find_combination(combination, combination_sum, index + 1)
        
        