import random
class RandomizedSet:
    def __init__(self):
        self.set = set()
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.set:
            return False
        self.set.add(val)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.set:
            self.set.remove(val)
            self.list.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return self.list[random.randint(0, len(self.set) - 1)]
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()