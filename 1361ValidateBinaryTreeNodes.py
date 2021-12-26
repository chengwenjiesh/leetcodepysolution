from typing import List
from collections import deque

class Solution:
    def validateBinaryTreeNodes2(self, n: int, leftChild: List[int], rightChild: List[int]):
        if not leftChild or not rightChild or len(leftChild) != len(rightChild):
            return False

        totalNodes = set(leftChild + rightChild)
        totalRoot = 0
        root = 0
        for i in range(n):
            if not i in totalNodes:
                root = i
                totalRoot += 1
        if totalRoot > 1 or totalRoot == 0:
            return False

        nodeQueue = deque([root])
        visited = {root}

        while nodeQueue:
            curr = nodeQueue.popleft()
            if leftChild[curr] != -1:
                if leftChild[curr] in visited:
                    return False
                else:
                    visited.add(leftChild[curr])
                    nodeQueue.append(leftChild[curr])
            if rightChild[curr] != -1:
                if rightChild[curr] in visited:
                    return False
                else:
                    visited.add(rightChild[curr])
                    nodeQueue.append(rightChild[curr])

        return len(visited) == n

    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        totalNodes = set(leftChild + rightChild)
        totalRoot = 0
        root = 0
        for i in range(n):
            if not i in totalNodes:
                root = i
                totalRoot += 1
        if totalRoot > 1 or totalRoot == 0:
            return False

        visited = set()
        if not self.findChild(n, root, leftChild, rightChild, visited):
            return False
        return len(visited) == n

    def findChild(self, n, root, leftChild, rightChild, visited):
        if root == -1:
            return True
        if root in visited:
            return False
        visited.add(root)
        return self.findChild(n, leftChild[root], leftChild, rightChild, visited) and \
               self.findChild(n, rightChild[root], leftChild, rightChild, visited)

if __name__ == '__main__':
    sol = Solution()
    print(sol.validateBinaryTreeNodes(4, [1,-1,3,-1], [2, -1, -1,-1]))
    print(sol.validateBinaryTreeNodes2(4, [1,-1,3,-1], [2, -1, -1,-1]))
