# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head == None:
            return None
        self.copyNext(head)
        self.copyRandom(head)
        dummyNode = head.next
        while head != None:
            tempNode = head.next
            head.next = head.next.next
            if head.next != None:
                tempNode.next = head.next.next
            head = head.next
        return dummyNode

    def copyNext(self, head):
        while head != None:
            node = RandomListNode(head.label)
            node.next = head.next
            head.next = node
            head = head.next.next

    def copyRandom(self, head):
        while head != None:
            if head.random != None:
                head.next.random = head.random.next
            head = head.next.next