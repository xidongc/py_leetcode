# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# cxd
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = slow = head
        tmp1 = tmp2 = None
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                # have loop
                tmp1 = head
                tmp2 = slow
                break

        while tmp1 is not tmp2:
            tmp1 = tmp1.next
            tmp2 = tmp2.next
        return tmp1
#     lmf
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
#         None/ 1 node cannot constitute a cycle
        if not head or not head.next:
            return None
        slow, fast = head,head.next
        while fast != slow:
            if fast == None or fast.next == None:
                return None
            slow = slow.next
            fast = fast.next.next
        node = head
        while node != slow.next:
            node = node.next
            slow = slow.next
        return node

