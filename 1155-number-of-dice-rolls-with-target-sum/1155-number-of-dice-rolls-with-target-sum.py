class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        rolls = [[0 for _ in range(target+1)] for _ in range(n+1)]
        
        for dice in range(1, n+1):
            for roll_total in range(dice, min(k * dice, target) + 1):
                if dice == 1:
                    rolls[dice][roll_total] = 1
                else:
                    end = roll_total - 1
                    start = max(1, roll_total - k)
                    rolls[dice][roll_total] = sum(rolls[dice-1][start:end+1])
        
        return rolls[n][target] % (10**9 + 7)