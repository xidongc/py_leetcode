class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:

    def create(self, list):
        head = h = ListNode(list[0])
        for l in list[1:]:
            n = ListNode(l)
            h.next = n
            h = h.next
        return head

    def show(self, head):
        if head:
            print(head.val)
            self.show(head.next)

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        num = 0
        stack = []
        before = ListNode(None)
        empty = ListNode(None)
        empty.next = head
        def helper(root):
            nonlocal num, stack, before
            while root:
                if num == m-1:
                    before = root
                elif m <= num < n:
                    stack.append(ListNode(root.val))
                elif num == n:
                    stack.append(ListNode(root.val))
                    while(stack):
                        before.next = stack.pop()
                        before = before.next
                elif num == n+1:
                    before.next = root
                root = root.next
                num += 1

        helper(empty)
        return empty.next

    def reverseBetween_2(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        empty = ListNode(None)
        empty.next = head
        num = 1

        def helper(root):
            nonlocal num
            while num < m:
                num += 1
                root = root.next
            print(root.val)
            pm = root.next
            while m <= num < n:
                h = pm.next
                pm.next = h.next
                h.next = root.next
                root.next = h
                num += 1
        helper(empty)
        return empty.next



