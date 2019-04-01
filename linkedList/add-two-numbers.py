# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None

        def helper(list1, list2):
            head = tmp = ListNode(None)
            extra = 0
            tmp_int = 0
            while list1 or list2:
                if list1 and list2:
                    val = list1.val + list2.val + extra
                    list1 = list1.next
                    list2 = list2.next
                elif list1:
                    val = list1.val + extra
                    list1 = list1.next
                elif list2:
                    val = list2.val + extra
                    list2 = list2.next

                if val >= 10:
                    val -= 10
                    tmp_int = 1
                else:
                    tmp_int = 0
                tmp.next = ListNode(val)
                extra = tmp_int
                tmp = tmp.next
            if extra == 1:
                tmp.next = ListNode(extra)
            return head.next

        return helper(l1, l2)
