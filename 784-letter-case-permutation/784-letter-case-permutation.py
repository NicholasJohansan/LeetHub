class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        self.permutations = []
        self.s = s
        self.s_length = len(s)
        self.make_permutations("", 0)
        return self.permutations
        
    def make_permutations(self, permutation: str, s_index: int) -> None:
        if len(permutation) == self.s_length:
            self.permutations.append(permutation)
        else:
            char = self.s[s_index]
            s_index += 1
            if char.isalpha():
                self.make_permutations(permutation + char.upper(), s_index)
                self.make_permutations(permutation + char.lower(), s_index)
            else:
                self.make_permutations(permutation + char, s_index)
        