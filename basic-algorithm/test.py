class TreeNode(object):

    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


class BT(object):

    def __init__(self):
        self.root = None

    def create_tree(self):
        # already created a tree
        pass

    def in_order_traversal(self):
        # morris traversal
        curr = self.root
        ret = list()
        while curr:
            if curr.left is None:
                ret.append(curr.val)
                curr = curr.right
            else:
                prev = curr.left
                while prev.right and prev.right is not curr:
                    prev = prev.right
                if prev.right is None:
                    prev.right = curr
                    curr = curr.left
                elif prev.right is curr:
                    prev.right = None
                    ret.append(curr.val)
                    curr = curr.right
        print(ret)
        return ret

    def post_traversal(self):
        self.__post_traversal(self.root)

    def __post_traversal(self, root):
        self.__post_traversal(root.left)
        self.__post_traversal(root.right)
        print(root.val)

    def pre_order_traversal(self):
        curr = self.root
        ret = list()
        stack = list()

        while curr or len(stack) > 0:
            while curr:
                stack.append(curr)
                ret.append(curr.val)
                curr = curr.left

            if len(stack) > 0:
                curr = stack.pop()
                curr = curr.right

        print(ret)
        return ret




