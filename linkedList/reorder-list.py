# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

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

    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return None

        slow = fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        fast = slow.next
        slow.next = None


        # fast -> None
        # head -> slow

        tmp = self.reverseList(fast)

        p = ListNode(None)
        slow = p

        while head and tmp:
            slow.next = head
            slow = slow.next
            head = head.next
            slow.next = tmp
            slow = slow.next
            tmp = tmp.next


        if head:
            slow.next = head
        if tmp:
            slow.next = tmp

        head = p.next
        return head

    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        else:
            h = self.reverseList(head.next)
            head.next.next = head
            head.next = None
            return h


s = Solution()
head = s.createList([1,2,3,4])
s.showList(s.reorderList(head))

#lmf 第一步找中点/第二反转链表/第三步把第二条链表的每个点插在第一个链表的点后面
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
        # find middle node
        if not head:
            return
        fast = slow = head
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        tmp = slow.next
        slow.next = None
        headB = self.reverseList(tmp)
        while headB != None:
            tmpA = head.next
            tmpB = headB.next
            head.next = headB
            headB.next = tmpA
            head = tmpA
            headB = tmpB

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