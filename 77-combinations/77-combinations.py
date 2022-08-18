class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.combinations = []
        self.n = n
        self.k = k
        self.make_combinations([], 1)
        return self.combinations
    
    def make_combinations(self, combination: List[int], curr: int) -> None:
        if len(combination) == self.k:
            self.combinations.append(combination)
            return
        else:
            for i in range(curr, self.n + 1):
                self.make_combinations(combination + [i], i + 1)
    
        