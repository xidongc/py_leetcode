from heapq import *

# n:length of each list; k: the number of lists
# solution 1: brute force: merge 2, then 3, then n
#             time complexity: 对于各种sort，比如mergesort所需要的时间
#               复杂度都一样，所以一个list就是n(log(n)
#               kn(log(nk))
#             space complexity: O(1)
# solution 2: 维护一个大小为k的heap, 每次pop出最小的，然后再从剩下的
#             list头里找最小的放入heap
#             时间：因为删除插入都是log(k),并总共有kn个点
#                   每个点都要经历一遍插入和删除
#                     knlog(k)
# solution 3: use divide and conquer
#                 复杂度： T(k) = 2T(k/2) + O(nk)， 每次都要做二分
#               O(nklogk)
#                 省去heap，但是会有递归heap的问题
#
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
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        if l1 is not None or l2 is not None:
            if l1 is not None:
                node.next = l1
            else:
                node.next = l2
        return dummy.next


# heapq method, python3 will report error due to ListNode not comparable
class Solution(object):

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        h = []
        for l in lists:
            if l:
                heappush(h, (l.val, l))
        dummy = ListNode(0)
        cur = dummy
        while h:
            v, node = heappop(h)
            if node.next:
                heappush(h, (node.next.val, node.next))
            cur.next = node
            cur = cur.next
        return dummy.next

