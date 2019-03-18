# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        new_head = head.next

        while head and head.next and head.next.next and head.next.next.next:
            q = head.next.next
            h = head.next.next.next
            head.next.next = head
            head.next = h
            head = q

        tmp = None
        if not head.next.next:
            head.next.next = head
        else:
            tmp = head.next.next
            head.next.next = head
        head.next = tmp


        return new_head