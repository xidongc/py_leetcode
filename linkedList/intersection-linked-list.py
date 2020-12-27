class Solution(object):

    # 或者把a.tail指向headb
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        a, b = headA, headB
        while a != b:  # either reaches None or same node
            # first iteration, swap start node so that they keep the difference
            a = a.next if a else headB
            b = b.next if b else headA
        return a
