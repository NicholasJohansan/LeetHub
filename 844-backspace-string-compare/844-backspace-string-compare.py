class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_pointer = len(s) - 1
        t_pointer = len(t) - 1
        backspaces = {"s": 0, "t": 0}
        while s_pointer >= 0 or t_pointer >= 0:
            while s_pointer >= 0:
                if s[s_pointer] == "#":
                    backspaces["s"] += 1
                    s_pointer -= 1
                elif backspaces["s"] > 0:
                    backspaces["s"] -= 1
                    s_pointer -= 1
                else:
                    break
            while t_pointer >= 0:
                if t[t_pointer] == "#":
                    backspaces["t"] += 1
                    t_pointer -= 1
                elif backspaces["t"] > 0:
                    backspaces["t"] -= 1
                    t_pointer -= 1
                else:
                    break
            if (s_pointer >= 0) != (t_pointer >= 0):
                return False
            if s_pointer >= 0 and t_pointer >= 0:
                if s[s_pointer] != t[t_pointer]:
                    return False
            s_pointer -= 1
            t_pointer -= 1
        return True