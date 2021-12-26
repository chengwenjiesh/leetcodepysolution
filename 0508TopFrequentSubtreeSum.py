from DataStructures import TreeNode

class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        topFreq = 0
        freqMap = {}
        result = []

    def findTreeSum(node):
        nonlocal topFreq
        if not node:
            return 0

        lSum, rSum = findTreeSum(node.left), findTreeSum(node.right)
        tSum = node.val + lSum + rSum
        if tSum not in freqMap:
            freqMap[tSum] = 1
        else:
            freqMap[tSum] += 1

        if freqMap[tSum] > topFreq:
            topFreq = freqMap[tSum]
            result.clear()
            result.append(tSum)
        elif freqMap[tSum] == topFreq:
            result.append(tSum)

        return tSum

        findTreeSum(root)
        return result


