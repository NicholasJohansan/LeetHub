class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        time = 0
        l = 0
        r = 0
        while r < len(colors):
            if colors[r] == colors[l]:
                r += 1
            elif colors[r] != colors[l]:
                times = [neededTime[i] for i in range(l, r)]
                maximum = max(times)
                time += sum(times) - maximum
                l = r
        times = [neededTime[i] for i in range(l, r)]
        maximum = max(times)
        time += sum(times) - maximum
        return time