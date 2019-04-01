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
        def helper(start):
            pre = start
            while start and start.next:
                if start.val != start.next.val :
                    pre = start
                    start = start.next
                else:
                    while start.next and start.val == start.next.val:
                        start = start.next
                    pre.next = start.next
                    start = pre.next

        empty = ListNode(None)
        empty.next = head
        helper(empty)
        return empty.next