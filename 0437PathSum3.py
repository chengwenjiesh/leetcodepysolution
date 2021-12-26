from DataStructures import TreeNode

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        return self.findAllPath(root, 0, {0:1}, targetSum)

    def findAllPath(self, root, prefix, prefixSumMap, target):
        if not root:
            return 0

        cnt = 0
        prefix += root.val
        cnt += prefixSumMap.get(prefix - target, 0)
        prefixSumMap[prefix] = prefixSumMap.get(prefix, 0) + 1

        cnt += self.findAllPath(root.left, prefix, prefixSumMap, target)
        cnt += self.findAllPath(root.right, prefix, prefixSumMap, target)

        prefixSumMap[prefix] -= 1
        if prefixSumMap[prefix] == 0:
            del prefixSumMap[prefix]

        return cnt

