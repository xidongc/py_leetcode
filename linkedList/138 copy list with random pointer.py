# Definition for singly-linked list with a random pointer.
# 两种解法，一种是hashmap用curnode做key，newnode做value
# 如果有空间限制的话，就用后面这种方法
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


#method 1
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
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


# method 2
class Solution(object):

    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return head
        newhead = RandomListNode(head.label)
        cur = newhead
        oldcur = head
        nodemap = dict()
        nodemap[head] = newhead
        while oldcur.next != None:
            cur.next = RandomListNode(oldcur.next.label)
            nodemap[oldcur.next] = cur.next
            oldcur = oldcur.next
            cur = cur.next
        oldcur = head
        cur = newhead
        while oldcur!= None:
            if oldcur.random:
                cur.random = nodemap[oldcur.random]
            oldcur = oldcur.next
            cur = cur.next
        return newhead


# Sol from Xidong
from collections import OrderedDict


#  Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution(object):

    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None

        oldnewmapping = OrderedDict()

        curr = head
        dummy = Node(0, None, None)
        newNode = dummy

        while curr:
            newNode.next = Node(curr.val, None, None)
            oldnewmapping[curr] = newNode.next
            newNode = newNode.next
            curr = curr.next

        for k, v in oldnewmapping.items():
            k.next = v
            v.random = k

        tmp = dummy.next
        while tmp:
            if tmp.random.random is None:
                tmp.random = None
            else:
                tmp.random = tmp.random.random.next
            tmp = tmp.next

        tmp = Node(0, None, None)
        for k in oldnewmapping:
            tmp.next = k
            tmp = tmp.next
        tmp.next = None

        return dummy.next