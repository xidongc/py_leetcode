# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        ha = headA
        while ha.next is not None:
            ha = ha.next
        ha.next = headB
        ret = self.getloopele(headA)
        ha.next = None
        if ret is None:
            return None
        else:
            return ret

    def getloopele(self, head):
        slow = fast = head
        tmp1 = tmp2 = None
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                tmp1 = head
                tmp2 = slow
                break
        while tmp1 is not tmp2:
            tmp1 = tmp1.next
            tmp2 = tmp2.next
        return tmp1

#lmf
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        a,b = headA, headB
        while a != b: #either reaches None or same node
            # first iteration, swap start node so that they keep the difference
            a = a.next if a != None else headB
            b = b.next if b != None else headA
        return a
# 或者把a.tail指向headb