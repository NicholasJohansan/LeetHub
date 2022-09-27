class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        forces = [0] * n
        
        force = 0
        for i in range(n):
            char = dominoes[i]
            if char == "R":
                force = n
            elif char == "L":
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] += force
        
        force = 0
        for i in range(n-1, -1, -1):
            char = dominoes[i]
            if char == "L":
                force = n
            elif char == "R":
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] -= force
        
        final = ""
        for force in forces:
            if force > 0:
                final += "R"
            elif force < 0:
                final += "L"
            else:
                final += "."
        
        return final
        