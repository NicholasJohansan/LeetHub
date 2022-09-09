class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        bin_left = bin(left)[2:]
        bin_right = bin(right)[2:]
        
        # prefix will never be common if the bit length is different
        if len(bin_left) < len(bin_right):
            return 0
        
        common_prefix = ""
        longest_prefix_found = False
        ans = "0b"
        for i in range(len(bin_left)):
            if longest_prefix_found:
                ans += "0"
                continue
            if bin_left[i] == bin_right[i]:
                common_prefix += bin_left[i]
            if bin_left[i] != bin_right[i]:
                ans += common_prefix + "0"
                longest_prefix_found = True
        if ans == "0b":
            ans += common_prefix
        return int(ans, 2)
        
        
        