from DataStructures import TreeNode
from typing import Optional
from typing import List

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs queue
        if not root:
            return []

        result = []
        levelQueue = deque([(root, 0)])

        while levelQueue:
            node, l = levelQueue.popleft()
            if l == len(result):
                result.append([node.val])
            else:
                result[l].append(node.val)

            if node.left:
                levelQueue.append((node.left, l + 1))
            if node.right:
                levelQueue.append((node.right, l + 1))

        return result


    def levelOrder1(self, root):
        # bfs frontier
        if not root:
            return root

        result = []
        up, down = [root], []
        while up:
            curr = []
            for node in up:
                curr.append(node.val)
                if node.left:
                    down.append(node.left)
                if node.right:
                    down.append(node.right)
            up, down = down, []
            result.append(curr)

        return result

    def levelOrder2(self, root):
        result = []
        self.dfs(root, 0, result)
        return result


    def dfs(self, root, level, result):
        if not root:
            return

        if level == len(result):
            result.append([root.val])
        elif level < len(result):
            result[level].append(root.val)

        self.dfs(root.left, level + 1, result)
        self.dfs(root.right, level + 1, result)


if __name__ == '__main__':
    sol = Solution()
    n1 = TreeNode(4)
    n2 = TreeNode(5)
    n3 = TreeNode(3, n1, n2)
    n4 = TreeNode(2)
    n1 = TreeNode(1, n3, n4)
    print(sol.levelOrder(n1))

