class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        p_count_dict = self.make_count_dict(p)
        s_count_dict = self.make_count_dict(s[0:len(p)])
        start_indices = []
        if p_count_dict == s_count_dict:
            start_indices.append(0)
        curr_index = 0
        next_index = curr_index + len(p)
        while next_index <= len(s):
            if s_count_dict[s[curr_index]] == 1:
                del s_count_dict[s[curr_index]]
            else:
                s_count_dict[s[curr_index]] -= 1
            if next_index < len(s):
                s_count_dict[s[next_index]] = s_count_dict.get(s[next_index], 0) + 1
            curr_index += 1
            next_index += 1
            if s_count_dict == p_count_dict:
                start_indices.append(curr_index)
        return start_indices
            
        
    def make_count_dict(self, word):
        d = {}
        for char in word:
            d[char] = d.get(char, 0) + 1
        return d
        