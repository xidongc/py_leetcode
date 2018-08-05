class Sol(object):
    def __init__(self):
        self.suc = None

    def in_order(self, head, num):
        if not head:
            return None
        int = []

        def helper(head):
            nonlocal int
            if head:
                self.helper(head.left)
                int.append(head.val)
                self.helper(head.right)
        helper(head)
        if num in int:
            return int[int.index(num)+1]


