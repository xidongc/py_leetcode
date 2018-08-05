# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def createList(self, list):
        h = head = ListNode(None)
        for l in list:
            head.next = ListNode(l)
            head = head.next
        return h.next

    def showList(self, head):
        while head is not None:
            print(head.val)
            head = head.next

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        slow = fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        fast = slow.next
        slow.next = None
        p1 = self.sortList(head)
        p2 = self.sortList(fast)
        return self.merge(p1, p2)

    def merge(self, list1, list2):
        h = p = ListNode(None)
        while list1 and list2:
            if list1.val <= list2.val:
                p.next = list1
                list1 = list1.next
            else:
                p.next = list2
                list2 = list2.next
            p = p.next

        if list1:
            p.next = list1
        if list2:
            p.next = list2
        return h.next

s = Solution()
head = s.createList(list=[3,2,1,4,5])
head2 = s.createList(list=[6,7,8])
head1 = s.sortList(head)
s.showList(head1)


