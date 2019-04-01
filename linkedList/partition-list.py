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

    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return None

        tmp2 = ListNode(None)
        tmp1 = ListNode(None)
        q = tmp1
        h = tmp2
        while head:
            if head.val >= x:
                tmp2.next = head
                tmp2 = tmp2.next
            else:
                tmp1.next = head
                tmp1 = tmp1.next
            head = head.next
        tmp1.next = h.next
        tmp2.next = None
        return q.next

s = Solution()
head = s.createList([1,4,3,2,5,2])
head1 = s.partition(head, 3)
s.showList(head1)

# lmf
def partition(self, head, x):
    """
    :type head: ListNode
    :type x: int
    :rtype: ListNode
    """
    h1, h2 = ListNode(0), ListNode(0)
    l1, l2 = h1, h2
    while head:
        if head.val < x:
            l1.next = head
            l1 = l1.next
        else:
            l2.next = head
            l2 = l2.next
        head = head.next
    #     为什么必须设none
    l2.next = None
    l1.next = h2.next
    return h1.next
# head: 1->3
# l1 0->1
# l2 0->3->1 l2指向的是3这个点，which has next node: 1