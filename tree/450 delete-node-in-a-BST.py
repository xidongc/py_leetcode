# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        # The target node does not exist, no change needed
        if not root:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            # Find the root.val == key
            # this root only has one subtree
            if root.right == None:
                return root.left
            elif root.left == None:
                return root.right
                # this root has both subtrees, find the minnode in its right tree as the new root, then delete this node
            minNode = self.findMin(root.right)
            root.val = minNode.val
            root.right = self.deleteNode(root.right, minNode.val)
        return root

    def findMin(self,node):
         while node.left:
             node = node.left
         return node

# 首先判断根节点是否为空。
# 定位
# 由于BST的左<根<右的性质，使得我们可以快速定位到要删除的节点，我们对于当前节点值不等于key的情况，根据大小关系对其左右子节点分别调用递归函数
# 删除
# 是否有一个子节点不存在，那么我们就将root指向另一个节点
# 左右子节点都不存在，那么root就赋值为空了
# 左右子节点都存在的情况，我们需要在右子树找到最小值，即右子树中最左下方的节点，然后将该最小值赋值给root，然后再在右子树中调用递归函数来删除这个值最小的节点