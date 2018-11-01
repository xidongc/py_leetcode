# Definition for singly-linked list.
# 从尾到头建立链表
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        x1, x2 = 0, 0
        while l1 != None:
            x1 = x1 * 10 + l1.val
            l1 = l1.next
        while l2 != None:
            x2 = x2 * 10 + l2.val
            l2 = l2.next
        x = x1 + x2
        head = ListNode(x)
        if x == 0:
            return head
        else:
            while x:
                a, b = x % 10, x // 10
                head.next, head.next.next = ListNode(a), head.next
                x = x // 10
        return head.next



