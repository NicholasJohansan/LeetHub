class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.visited = set()
        provinces = 0
        for i in range(len(isConnected)):
            if i not in self.visited:
                provinces += 1
                self.traverse(isConnected[i], isConnected)
        return provinces
        
    def traverse(self, neighbouring_connections: List[int], connections: List[List[int]]):
        for i in range(len(neighbouring_connections)):
            connected = neighbouring_connections[i]
            if connected and i not in self.visited:
                self.visited.add(i)
                self.traverse(connections[i], connections)