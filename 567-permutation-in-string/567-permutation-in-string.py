class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_char_count = self.make_count_dictionary(s1)
        s2_char_count = {}
        start = 0
        for end in range(len(s2)):
            char = s2[end]
            while not self.is_sub(s2_char_count, s1_char_count):
                another_char = s2[start]
                s2_char_count[another_char] -= 1
                if s2_char_count[another_char] == 0:
                    s2_char_count.pop(another_char)
                start += 1
            s2_char_count[char] = s2_char_count.get(char, 0) + 1
            if s1_char_count == s2_char_count:
                return True
        return False
    
    def is_sub(self, sub_dict: dict[str, int], super_dict: dict[str, int]):
        keys_is_subset = set(sub_dict.keys()).issubset(set(super_dict.keys()))
        if not keys_is_subset: return False
        return all([sub_dict.get(key, 0) <= super_dict[key] for key in super_dict.keys()])
    
    def make_count_dictionary(self, string: str) -> dict[str, int]:
        count_dictionary = dict()
        for char in string:
            count_dictionary[char] = count_dictionary.get(char, 0) + 1
        return count_dictionary
        