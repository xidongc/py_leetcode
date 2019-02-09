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
#         p = head
#         head = self.reverseList(p.next)
#         p.next.next = p
#         p.next = None
#         return head

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