class LinkedNode(object):

    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList(object):

    def __init__(self):
        self.head = None

    def reverse(self):
        # assume we have a linked list
        if self.head is None:
            print("you really need to insert first")
            return None
        self.head = self.__reverse(self.head)

    def create_linked_list(self, arr):
        self.head = LinkedNode(arr[0])
        curr = self.head
        for ele in arr[1:]:
            curr.next = LinkedNode(ele)
            curr = curr.next

    def show(self):
        curr = self.head
        ret = []
        while curr is not None:
            print(curr.val)
            ret.append(curr.val)
            curr = curr.next
        #print(ret)
        return ret

    def __reverse(self, node):
        if node.next is None:
            return node
        prev = self.__reverse(node.next)
        head = prev
        node.next.next = node
        node.next = None
        return prev

s = LinkedList()
s.create_linked_list([1,4,3,2,5,6,1,3,4])
#s.show()
s.reverse()
s.show()