# 第一步找中点/第二反转链表/第三步把第二条链表的每个点插在第一个链表的点后面
class Solution(object):

    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        # corner case
        if not head or not head.next:
            return head

        # find middle node
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # small trick to set the end of first to None
        tmp = slow.next
        slow.next = None

        # reverse slow
        newhead = self.reverseList(tmp)

        # merge
        while newhead:
            n1 = head.next
            n2 = newhead.next
            head.next = newhead
            newhead.next = n1
            head = n1
            newhead = n2

    def reverseList(self, head):
        if not head or not head.next:
            return head
        prev = head
        cur = head.next
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        head.next = None
        return prev
