from linkedList.listnode import ListNode


class Solution(object):

    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # corner case
        if head is None:
            return head

        odd = head
        # should fix even head
        mark = even = head.next

        while odd and even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = mark

        if even:
            even.next = None

        return head
