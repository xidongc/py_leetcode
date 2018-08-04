# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = slow = head
        tmp1 = tmp2 = None
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                # have loop
                tmp1 = head
                tmp2 = slow
                break

        while tmp1 is not tmp2:
            tmp1 = tmp1.next
            tmp2 = tmp2.next
        return tmp1

