vowels = "aeiou"

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        front = s[:len(s) // 2]
        back = s[len(s) // 2:]
        return self.get_vowel_occurences(front) == self.get_vowel_occurences(back)
    
    def get_vowel_occurences(self, s):
        occurences = 0
        for char in s:
            if char.lower() in vowels:
                occurences += 1
        return occurences