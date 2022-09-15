class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        counts = {}
        for num in changed:
            counts[num] = counts.get(num, 0) + 1
        
        orig = []
        nums = sorted(changed, reverse=True)
        
        while nums:
            num = nums.pop()
            if num not in counts:
                continue
                
            doubled = num * 2
            if doubled not in counts:
                return []
            
            orig.append(num)
            counts[num] -= 1
            
            # special condition for zero
            if counts[doubled] < 1:
                return []
            
            counts[doubled] -= 1
            
            
            if counts[num] <= 0:
                del counts[num]
            if doubled in counts and counts[doubled] <= 0:
                del counts[doubled]
        
        return orig