class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        can_segment = [False for i in range(len(s) + 1)]
        can_segment[0] = True
        seen_word = ""
        for i in range(len(s)):
            seen_word += s[i]
            for word in wordDict:
                seen_length = i + 1
                word_length = len(word)
                if seen_length < word_length:
                    continue
                seen = seen_word[seen_length-word_length:seen_length]
                if seen == word:
                    pre_can_segment = can_segment[seen_length-word_length]
                    if pre_can_segment:
                        can_segment[seen_length] = pre_can_segment
                        break
        return can_segment[len(s)]
                
        