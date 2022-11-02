class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        
        for string in strs:
            anagram_hash = self.get_hash(string)
            if anagram_hash in anagrams:
                anagrams[anagram_hash].append(string)
            else:
                anagrams[anagram_hash] = [string]
        
        return list(anagrams.values())
        
    def get_hash(self, string):
        anagram_hash = [0 for _ in range(26)]
        for char in string:
            index = ord(char) - 97
            anagram_hash[index] += 1
        return tuple(anagram_hash)