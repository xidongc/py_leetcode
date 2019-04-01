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

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def prepare(l1, l2):
            tmp1 = l1
            tmp2 = l2
            while l1 or l2:
                if l1 and l2:
                    l1 = l1.next
                    l2 = l2.next
                elif not l1:
                    l2 = l2.next
                    s = ListNode(0)
                    s.next = tmp1
                    tmp1 = s
                elif not l2:
                    l1 = l1.next
                    s = ListNode(0)
                    s.next = tmp2
                    tmp2 = s
            h = ListNode(0)
            s = ListNode(0)
            s.next = tmp2
            tmp2 = s
            h.next = tmp1
            tmp1 = h
            self.showList(tmp1)
            self.showList(tmp2)
            return tmp1, tmp2

        extra = 0
        def helper(l1, l2):
            nonlocal extra
            if not l1.next and not l2.next:
                ret = l1.val + l2.val
                if ret >= 10:
                    ret -= 10
                    extra = 1
                return ListNode(ret)
            hd = helper(l1.next, l2.next)
            num = l1.val + l2.val + extra
            if num >= 10:
                num -= 10
                extra = 1
            else:
                extra = 0
            p = ListNode(num)
            p.next = hd
            return p

        l1, l2 = prepare(l1, l2)
        x = helper(l1, l2)
        if x.val == 0:
            return x.next
        else:
            return x

s = Solution()
head1 = s.createList([7,2,4,3])
head2 = s.createList([5,6,4])
head3 = s.addTwoNumbers(head1, head2)
s.showList(head3)

