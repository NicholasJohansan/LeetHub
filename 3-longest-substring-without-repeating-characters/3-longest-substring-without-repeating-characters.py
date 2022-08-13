class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        string_set = set()
        max_length = 0
        for end in range(len(s)):
            char = s[end]
            while char in string_set:
                string_set.remove(s[start])
                start += 1
            string_set.add(char)
            length = end - start + 1
            if length > max_length:
                max_length = length
        return max_length
        
            
        