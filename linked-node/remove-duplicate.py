# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        start = head
        if not head:
            return head
        while head.next is not None:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return start