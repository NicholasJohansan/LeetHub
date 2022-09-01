class Solution:
    MAP = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    
    def letterCombinations(self, digits: str) -> List[str]:
        self.digits = digits
        if not digits:
            return []
        self.combinations = []
        self.find_combination("", 0)
        return self.combinations
        
    def find_combination(self, combination, index):
        if index == len(self.digits):
            self.combinations.append(combination)
            return
        digit = self.digits[index]
        letters = Solution.MAP[digit]
        for letter in letters:
            self.find_combination(combination + letter, index + 1)
            