# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        dummy = ListNode(0)
        dummy.next = head
        head = dummy

        while head is not None:
            head = self.findnextK(head, k)

        return dummy.next

    def findnextK(self, head, k):
        # n0, n1......nk nm
        # head = nk
        # currently head: n0

        nk = head

        for _ in range(k):
            nk = nk.next
            if nk is None:
                return None

        nm = nk.next
        prev = head.next
        curr = head.next.next
        prev.next = nm
        h1 = prev

        while curr is not nm:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        head.next = prev
        return h1

    def printlist(self, head):
        curr = head

        while curr is not None:
            print(curr.val)
            curr = curr.next

    def reverse_node(self, head):
        prev = head
        curr = head.next
        prev.next = None
        while curr is not None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev

    def create_list(self):
        head = prev = ListNode(1)
        for i in range(2, 6):
            tmp = ListNode(i)
            prev.next = tmp
            prev = tmp
        return head


s = Solution()
head = s.create_list()

head = s.reverseKGroup(head, 2)
s.printlist(head)