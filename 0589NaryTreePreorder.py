# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node'):
        result = []
        self.preorderDFS(root, result)
        return result

    def preorderDFS(self, root, result):
        if root:
            result.append(root.val)
            for child in root.children:
                self.preorderDFS(child, result)

