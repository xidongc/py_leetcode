from linkedList.listnode import ListNode


class Solution(object):

    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # corner case
        if not head or not head.next:
            return head
        odd = head
        mark = even = head.next
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = mark
        return head
