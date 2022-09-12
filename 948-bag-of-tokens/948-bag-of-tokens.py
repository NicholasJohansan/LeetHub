class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        l = 0
        r = len(tokens) - 1
        score = 0
        max_score = 0
        tokens.sort()
        while (l <= r) and (power >= tokens[l] or score >= 1):
            while l <= r and power >= tokens[l]:
                power -= tokens[l]
                score += 1
                l += 1
            max_score = max(max_score, score)
            if l <= r and score >= 1:
                power += tokens[r]
                score -= 1
                r -= 1
        return max_score
            
        