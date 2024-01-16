class BSTIterator:
    """
    @param: root: The root of binary tree.
    """

    def __init__(self, root):
        self.stack = []
        self.get_left_node(root)  # insert all the left nodes in a stack

    def get_left_node(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    """
    @return: True if there has next node, or false
    """

    def hasNext(self):
        return len(self.stack) > 0

    """
    @return: return next node
    """

    def _next(self):
        if self.hasNext():
            ele = self.stack.pop()
            self.get_left_node(ele.right)  # insert the right nodes
            return ele
        return None
