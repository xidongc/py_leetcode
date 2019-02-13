# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# 递归
# class Solution:
#     def reverseList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         if not head or not head.next:
#             return head
# 这个newhead在递归函数里不起作用，所以每次都返回这个newhead
#         newhead = self.reverseList(p.next)
#         head.next.next = head
#         head.next = None
#         return newhead
#非递归
class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
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
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
s = Solution()
print(s.reverseList(head))