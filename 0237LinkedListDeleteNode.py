from DataStructures import ListNode

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

if __name__ == '__main__':
    sol = Solution()
    t4 = ListNode(4)
    t3 = ListNode(3, t4)
    t2 = ListNode(2, t3)
    t1 = ListNode(1, t2)
    sol.deleteNode(t2)
    print(t1)

