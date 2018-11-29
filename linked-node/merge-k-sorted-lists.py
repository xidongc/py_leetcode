# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # cxd 你这个解法超时了哇
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
# solution2: use heapq, push all the linkedlists into the heapq,
# then keep pop the smallest ones and connects them
# lmf
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return lists
        return self.mergehelper(lists, 0, len(lists) - 1)

    def mergehelper(self, lists, start, end):
        if start == end:
            return lists[start]
        mid = (start + end) // 2
        left = self.mergehelper(lists, start, mid)
        right = self.mergehelper(lists, mid + 1, end)
        return self.mergeTwoLists(left, right)

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNodeingle
        :rtype: ListNode
        """
        dummy = ListNode(None)
        node = dummy
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        if l1 != None or l2 != None:
            if l1 != None:
                node.next = l1
            else:
                node.next = l2
        return dummy.next

