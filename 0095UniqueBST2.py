from DataStructures import TreeNode

class Solution:
    def generateTrees(self, n: int):
        if n < 1:
            return []
        return self.buildTrees(1, n)


    def buildTrees(self, start, end):
        if start > end:
            return [None]

        if start == end:
            return [TreeNode(start)]

        result = []
        for i in range(start, end + 1):
            leftSub = self.buildTrees(start, i - 1)
            rightSub = self.buildTrees(i + 1, end)
            for l in leftSub:
                for r in rightSub:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    result.append(root)

        return result

if __name__ == '__main__':
    sol = Solution()
    print(sol.generateTrees(3))

