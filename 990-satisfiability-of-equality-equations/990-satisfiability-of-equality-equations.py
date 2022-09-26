class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        unequals = []
        self.roots = {}
        for equation in equations:
            equal = equation[1] == "="
            x = equation[0]
            y = equation[3]
            if not equal:
                unequals.append((x, y))
            else:
                root_x = self.root_of(x)
                root_y = self.root_of(y)
                if root_x != root_y:
                    self.roots[root_x] = root_y
        unequals_assertions = []
        for x, y in unequals:
            unequals_assertions.append(self.root_of(x) != self.root_of(y))
        return all(unequals_assertions)
        
    def root_of(self, var):
        root = var
        while root in self.roots:
            root = self.roots[root]
        return root