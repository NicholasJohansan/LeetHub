class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        answers = []
        even_sum = sum([num for num in nums if num % 2 == 0])
        for query in queries:
            val, i = query
            num = nums[i]
            even_before = num % 2 == 0
            nums[i] += val
            even_after = nums[i] % 2 == 0
            if even_before and not even_after:
                even_sum -= num
            elif not even_before and even_after:
                even_sum += nums[i]
            elif even_before and even_after:
                even_sum += val
            answers.append(even_sum)
        return answers
        