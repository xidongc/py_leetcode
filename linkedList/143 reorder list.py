# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        # 起码需要两个点
        if head == None or head.next == None:
            return
        slow, fast = head, head
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
        # 1->2->3->4->5
        # low = 3
        # 1->2->3->4->5->6
        # low = 3

        # 1->2->3->6->5->4
        prevMiddle = slow
        prevCurrent = prevMiddle.next
        while prevCurrent.next != None:
            current = prevCurrent.next
            prevCurrent.next = current.next
            current.next = prevMiddle.next
            prevMiddle.next = current

        # 1->6->2->5->3->4
        p1 = head
        p2 = prevMiddle.next
        # 跳出条件
        while p1 != prevMiddle:
            prevMiddle.next = p2.next
            p2.next = p1.next
            p1.next = p2
            p1 = p2.next
            p2 = prevMiddle.next
