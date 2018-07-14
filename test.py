import queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree(object):

    def createTree(self, list):
        root = TreeNode(list.pop(0))
        q = queue.Queue()
        q.put(root)
        while list and not q.empty():
            current = q.get()
            if len(list) >=2:
                current.left = TreeNode(list.pop(0))
                current.right = TreeNode(list.pop(0))
            else:
                current.left = TreeNode(list.pop(0))
            q.put(current.left)
            q.put(current.right)
        return root

    def showTree(self, root):
        if not root:
            return
        print(root.val)
        self.showTree(root.left)
        self.showTree(root.right)


l = [1,2,3,4,5,6,7,8]
t = Tree()
root = t.createTree(l)
a = t.in_order_traveral(root)
