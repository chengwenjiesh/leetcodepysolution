class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        visited = {}
        self.dfs(root, visited)
        return visited[root]
    
    def dfs(self, root, visited):
        visited[root] = Node(root.val)
        
        for child in root.children:
            if child not in visited:
                self.dfs(child, visited)
            visited[root].children.append(visited[child])


