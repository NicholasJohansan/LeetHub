class Solution:
    def countPrimes(self, n: int) -> int:
        is_prime = [1 for _ in range(n)]
        prime_count = 0
        for num in range(2, n):
            if not is_prime[num]:
                continue
            for i in range(num * 2, n, num):
                is_prime[i] = 0
            prime_count += 1
        return prime_count