class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:        
        min_change = [float('inf') for i in range(amount + 1)]
        min_change[0] = 0
        
        for i in range(1, amount + 1):
            potential = [min_change[i]]
            for coin in coins:
                if coin <= i:
                    potential.append(min_change[i - coin] + 1)
            min_change[i] = min(potential)
        
        if min_change[amount] == float('inf'):
            return -1
        return min_change[amount]