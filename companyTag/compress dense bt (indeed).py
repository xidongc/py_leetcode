class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class BTreeToArray:
    # sparse tree use map/lc297
    # dense tree
    def compress_dense_tree(self, root):
        height = self.get_height(root)
        res = [0] * (2**height)
        if height == 0:
            return res
        indexQueue = [0]
        queue = [root]
        while queue:
            node = queue.pop(0)
            index = indexQueue.pop(0)
            res[index] = node.val
            if node.left:
                queue.append(node.left)
                indexQueue.append(index*2+1)
            if node.right:
                queue.append(node.right)
                indexQueue.append(index*2+2)
        return res
    def get_height(self,root):
        if not root:
            return 0
        return max(self.get_height(root.left),self.get_height(root.right)) + 1