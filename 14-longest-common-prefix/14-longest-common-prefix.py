class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        lcp = ""
        for i in range(max([len(str) for str in strs])):
            try:
                char = strs[0][i]
            except:
                return lcp
            for str in strs:
                try:
                    if str[i] != char:
                        return lcp
                except:
                    return lcp
            lcp += char
        return lcp
                
        