# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node is not None:
            node.val = node.next.val
            curr = node
            node = node.next
            if node is not None:
                curr.next = node.next
            else:
                curr.next = None