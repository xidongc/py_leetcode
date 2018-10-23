class TreeNode(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree(object):

    def __init__(self):
        self.root = None

    def insert(self, val):
        self.root = self.__insert(self.root, val)

    def insert_node(self, val):
        if self.root is None:
            self.root = TreeNode(val)
            return
        curr = self.root
        prev = None
        while curr is not None:
            prev = curr
            if curr.val > val:
                curr = curr.left
            else:
                curr = curr.right
        if prev.val > val:
            prev.left = TreeNode(val)
        else:
            prev.right = TreeNode(val)
        return

    def __insert(self, node, val):
        if node is None:
            node = TreeNode(val)
            return node
        if val < node.val:
            node.left = self.__insert(node.left, val)
        else:
            node.right = self.__insert(node.right, val)
        return node

    def delete(self, val):
        self.__delete(val, self.root)

    def __delete(self, val, node):
        if node is None:
            return None
        if node.val < val:
            node.right = self.__delete(val, node.right)
        elif node.val > val:
            node.left = self.__delete(val, node.left)
        else:
            # return the largest in left sub-tree
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                lx = self.__find_lx(node.left)
                lx.left = self.__delete_lx(node.left)
                lx.right = node.right
                return lx
        return node

    def __find_lx(self, node):
        if node.right is None:
            return node
        curr = node.right
        while curr.right is not None:
            curr = curr.right
        return curr

    def __delete_lx(self, node):
        if node.right is None:
            return node.left
        curr = node.right
        prev = node
        while curr.right is not None:
            prev = curr
            curr = curr.right
        prev.right = None
        return node

    def create_tree(self, arr):
        for ele in arr:
            self.insert(ele)

    def search(self, val):
        curr = self.root
        prev = None
        while curr is not None:
            if curr.val == val:
                return curr, prev
            elif val < curr.val:
                prev = curr
                curr = curr.left
            else:
                prev = curr
                curr = curr.right
        if curr is None:
            print("not found")
            return None

    def __in_order(self, root):
        if root is None:
            return
        self.__in_order(root.left)
        print(root.val)
        self.__in_order(root.right)

    def in_order(self):
        self.__in_order(self.root)

    def traverse_in(self):
        ret = list()
        stack = list()
        curr = self.root

        while curr or len(stack) > 0:
            while curr:
                stack.append(curr)
                curr = curr.left
            if len(stack) > 0:
                curr = stack.pop()
                ret.append(curr.val)
                curr = curr.right

        print(ret)
        return ret

    def pre_order_non_recur(self):
        stack = list()
        ret = list()
        curr = self.root

        while len(stack) > 0 or curr:
            while curr:
                ret.append(curr.val)
                stack.append(curr)
                curr = curr.left
            if len(stack) > 0:
                curr = stack.pop()
                curr = curr.right
        print(ret)
        return ret

    def morris_in_order(self):
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

    def morris_pre_order(self):
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
                    ret.append(curr.val)
                    curr = curr.left
                elif prev.right is curr:
                    prev.right = None
                    curr = curr.right
        print(ret)
        return ret

    def post_traversal(self):
        ret = []
        self.__post_traversal(self.root, ret)
        print(ret)
        return ret

    def __post_traversal(self, root, ret):
        if root is None:
            return
        self.__post_traversal(root.left, ret)
        self.__post_traversal(root.right, ret)
        ret.append(root.val)

    def post_order_traversal(self):
        curr = self.root
        stack = list()
        ret = list()

        while stack or curr:
            while curr:
                stack.append(curr)
                ret.append(curr.val)
                curr = curr.right
            if stack:
                curr = stack.pop()
                curr = curr.left
        print(ret[::-1])
        return ret[::-1]

s = BinaryTree()
s.create_tree([1,5,3,7,6,9,8,5,11,2,21,32,43,54,65,76,87])
#s.in_order()
#print("###")
#s.delete(54)
#s.in_order()
s.traverse_in()
s.pre_order_non_recur()
s.morris_pre_order()
s.post_traversal()
s.post_order_traversal()