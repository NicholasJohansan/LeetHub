class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.combination_length = n * 2
        self.n = n
        self.combinations = []
        self.find_combination("", 0, 0)
        return self.combinations
        
    def find_combination(self, combination, num_open, num_close):
        if len(combination) == self.combination_length:
            self.combinations.append(combination)
            return
        if num_open < self.n:
            self.find_combination(combination + "(", num_open + 1, num_close)
        if num_close < num_open:
            self.find_combination(combination + ")", num_open, num_close + 1)