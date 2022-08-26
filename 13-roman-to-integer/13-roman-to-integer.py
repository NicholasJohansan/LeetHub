lazy_mapping = {
    "IV": "IIII",
    "IX": "VIIII",
    "XL": "XXXX",
    "XC": "LXXXX",
    "CD": "CCCC",
    "CM": "DCCCC"
}

numeral_mapping = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

class Solution:
    def romanToInt(self, s: str) -> int:
        for key, value in lazy_mapping.items():
            s = s.replace(key, value)
        num = 0
        for char in s:
            num += numeral_mapping[char]
        return num