# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node'):
        result = []
        self.postorderDFS(root, result)
        return result

    def postorderDFS(self, root, result):
        if root:
            for child in root.children:
                self.postorderDFS(child, result)
            result.append(root.val)

