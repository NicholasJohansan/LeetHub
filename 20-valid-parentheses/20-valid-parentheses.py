class Solution:
    def isValid(self, s: str) -> bool:
        bracket_stack = []
        opening_map = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        closing_brackets = [")", "]", "}"]
        for char in s:
            if char in closing_brackets:
                br_open = opening_map[char]
                if len(bracket_stack) == 0:
                    return False
                if bracket_stack.pop() != br_open:
                    return False
            else:
                bracket_stack.append(char)
        return len(bracket_stack) == 0
            