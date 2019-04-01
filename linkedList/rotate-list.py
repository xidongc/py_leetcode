# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0:
            return head

        tmp = head
        n = 1
        while tmp.next is not None:
            tmp = tmp.next
            n += 1
        tmp.next = head

        n = (n-k)%n
        for i in range(n):
            tmp = tmp.next
        head = tmp.next
        tmp.next = None
        return head
