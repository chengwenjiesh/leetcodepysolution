class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        visited = {}
        self.dfs(node, visited)
        return visited[node]
        
    def dfs(self, node, visited):
        visited[node] = Node(node.val)
        
        for n in node.neighbors:
            if n not in visited:
                self.dfs(n, visited)
            visited[node].neighbors.append(visited[n])


if __name__ == '__main__':
    sol = Solution()
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n1.neighbors = [n2,n4]
    n2.neighbors = [n1,n3]
    n2.neighbors = [n2,n4]
    n4.neighbors = [n1,n3]
    res = sol.cloneGraph(n1)


