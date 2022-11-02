class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = -1
        char_index = 0
        while char_index < len(haystack):
            char = haystack[char_index]
            if char == needle[0]:
                index = char_index
                count = 1
                ci = char_index + 1
                while count < len(needle) and ci < len(haystack):
                    next_char = haystack[ci]
                    if next_char != needle[count]:
                        break
                    count += 1
                    ci += 1
                if count == len(needle):
                    return index
                index = -1
            char_index += 1
        return index 