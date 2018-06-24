class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Sol(object):
    def __init__(self, ls):
        self.root = h = Node(ls[0])
        self.list = [self.root]
        for l in ls[1:]:
            tmp = Node(l)
            h.next = tmp
            self.list.append(tmp)
            h = h.next

    def prt(self, root):
        while root:
            print(root.val)
            root = root.next

    def getlist(self):
        for l in self.list:
            print(l.val)


def reverse_official(from_node, to_node):
    if from_node is to_node:
        return None
    x = from_node
    y = from_node.next
    while True:
        z = y.next
        y.next = x
        x = y
        y = z
        if x is to_node:
            break
    return x


def get_reverse(from_node, to_node):
    dummy = Node(-1)
    dummy.next = from_node

    cur = dummy.next
    post = Node(-1)
    while post is not to_node:
        post = cur.next
        cur.next = post.next
        post.next = dummy.next
        dummy.next = post

    del dummy, cur, post

    return to_node


s = Sol([1, 2, 3, 4, 5])
print("Test", s.list[4].val)
node = get_reverse(s.list[0], s.list[4])
node = get_reverse(s.list[4], s.list[0])
node = reverse_official(s.list[0], s.list[4])
s.prt(node)
