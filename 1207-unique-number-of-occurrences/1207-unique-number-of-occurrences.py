class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurences = {}
        for num in arr:
            occurences[num] = occurences.get(num, 0) + 1
        encountered = set()
        for num_occured in occurences.values():
            if num_occured in encountered:
                return False
            encountered.add(num_occured)
        return True