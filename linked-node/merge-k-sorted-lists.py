# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        while len(lists) >= 2:
            lists.append(self.mergeTwo(lists.pop(), lists.pop()))
        if len(lists) == 1:
            return lists[0]
        else:
            return None

    def mergeTwo(self, head1, head2):
        head = p = ListNode(None)
        while head1 and head2:
            if head1.val <= head2.val:
                p.next = head1
                head1 = head1.next
            else:
                p.next = head2
                head2 = head2.next
            p = p.next
        if head1:
            p.next = head1
        if head2:
            p.next = head2
        return head.next
    