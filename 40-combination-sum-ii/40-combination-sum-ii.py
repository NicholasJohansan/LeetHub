class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = sorted(candidates)
        self.target = target
        self.combinations = []
        self.find_combination([], 0, 0)
        return self.combinations
        
    def find_combination(self, combination, combination_sum, index):
        if combination_sum == self.target:
            if combination not in self.combinations:
                self.combinations.append(combination)
                
        prev = 0
        for i in range(index, len(self.candidates)):
            num = self.candidates[i]
            if num == prev:
                continue
            prev = num
            if combination_sum + num <= self.target:
                self.find_combination(combination + [num], combination_sum + num, i + 1)
            else:
                break