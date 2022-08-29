class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.paths = []
        n = len(graph)
        self.goal = n - 1
        self.search_path(graph, 0, [0])
        return self.paths
                    
    def search_path(self, graph, start, path):
        if start == self.goal:
            self.paths.append(path)
            return
        for dest_node in graph[start]:
            self.search_path(graph, dest_node, path + [dest_node])