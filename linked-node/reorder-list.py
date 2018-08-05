# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def createList(self, list):
        h = head = ListNode(None)
        for l in list:
            head.next = ListNode(l)
            head = head.next
        return h.next

    def showList(self, head):
        while head is not None:
            print(head.val)
            head = head.next

    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return None

        slow = fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        fast = slow.next
        slow.next = None


        # fast -> None
        # head -> slow

        tmp = self.reverseList(fast)

        p = ListNode(None)
        slow = p

        while head and tmp:
            slow.next = head
            slow = slow.next
            head = head.next
            slow.next = tmp
            slow = slow.next
            tmp = tmp.next


        if head:
            slow.next = head
        if tmp:
            slow.next = tmp

        head = p.next
        return head

    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        else:
            h = self.reverseList(head.next)
            head.next.next = head
            head.next = None
            return h


s = Solution()
head = s.createList([1,2,3,4])
s.showList(s.reorderList(head))
