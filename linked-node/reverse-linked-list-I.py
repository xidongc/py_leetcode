# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    # recursive
    def reverseListRecursive(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        newhead = self.reverseList(p.next)
        head.next.next = head
        head.next = None
        return newhead

    # non recursive
    def reverseListNonRecursive(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        prev = None
        cur = head

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        return prev

    # mainly used for debug
    def printLinkedList(self, head):
        curr = head
        while curr:
            print(curr.val)
            curr = curr.next

