class Node(object):

    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


class Tree(object):

    def __init__(self, list):
        self.list = list

    def create_tree(self):
        if not self.list:
            return None
        self.list = list(map(Node, self.list))
        length = len(self.list)

        for i, x in enumerate(self.list[0:length//2+1]):
            if i*2+1 < length and self.list[i*2+1]:
                x.left = self.list[i*2+1]
            if i*2+2 < length and self.list[i*2+2]:
                x.right = self.list[i*2+2]

        return self.list[0]


class MorrisTraversal(object):

    def __init__(self, root):
        self.root = root

    def in_traversal(self):
        current = self.root
        in_order = []

        while current:
            if not current.left:
                in_order.append(current.val)
                current = current.right
            else:
                help = current.left
                while help.right and help.right is not current:
                    help = help.right
                if help.right is None:
                    help.right = current
                    current = current.left
                else:
                    help.right = None
                    in_order.append(current.val)
                    current = current.right
        return in_order

    def pre_traversal(self):
        current = self.root
        pre_order = []
        while current is not None:
            if current.left is None:
                pre_order.append(current.val)
                current = current.right
            else:
                pre = current.left
                while pre.right and pre.right is not current:
                    pre = pre.right
                if pre.right is None:
                    pre.right = current
                    pre_order.append(current.val)
                    current = current.left
                else:
                    pre.right = None
                    current = current.right

        return pre_order

    def post_traversal(self):
        post_order = []

        def get_reverse(from_node, to_node):
            if from_node == to_node:
                return None

            dummy = Node(-1)
            dummy.right = from_node
        
            cur = dummy.right
            post = Node(-1)
            while post is not to_node:
                post = cur.right
                cur.right = post.right
                post.right = dummy.right
                dummy.right = post
        
            del dummy, cur, post
        
            return to_node

        def reverse(from_node, to_node):
            if from_node is to_node:
                pass

            get_reverse(from_node, to_node)
            x = to_node
            while x is not from_node:
                post_order.append(x.val)
                x = x.right
            post_order.append(x.val)
            get_reverse(to_node, from_node)

        dummy = Node(0)
        dummy.left = self.root
        current = dummy
        while current:
            if not current.left:
                current = current.right

            else:
                prev = current.left
                while prev.right and prev.right is not current:
                    prev = prev.right
                if prev.right is None:
                    prev.right = current
                    current = current.left
                else:
                    reverse(current.left, prev)
                    prev.right = None
                    current = current.right
        return post_order


a = [1,2,3,4,5,6,7,8,9]
t = Tree(a)
root = t.create_tree()
s = MorrisTraversal(root)
print(s.in_traversal())
print(s.pre_traversal())
print(s.post_traversal())