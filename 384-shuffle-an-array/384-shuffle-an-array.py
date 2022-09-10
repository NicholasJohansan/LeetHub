from random import choice as randchoice
from random import randint

class Solution:

    def __init__(self, nums: List[int]):
        self.orig = nums[:]
        self.nums = nums

    def reset(self) -> List[int]:
        self.nums = self.orig[:]
        return self.nums
        

    def shuffle(self) -> List[int]:
        indices = list(range(len(self.orig)))
        for i in range(len(self.nums)):
            index = indices.pop(randint(0, len(indices) - 1))
            self.nums[i] = self.orig[index]
        return self.nums
            
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()