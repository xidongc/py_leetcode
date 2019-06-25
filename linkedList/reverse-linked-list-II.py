class Solution(object):

    def reverseBetween(self, head, m: int, n: int):
        if not head:
            return head

        dummy = ListNode(0)
        dummy.next = head

        curr = dummy

        for _ in range(m - 1):
            if curr.next:
                curr = curr.next

        prev = curr
        start = prev.next

        for _ in range(n - m + 1):
            if curr.next:
                curr = curr.next

        last = curr
        after = curr.next

        prev.next = last

        p1 = after
        p2 = start
        while p2 is not after:
            p3 = p2.next
            p2.next = p1
            p1 = p2
            p2 = p3

        start.next = after
        return dummy.next
