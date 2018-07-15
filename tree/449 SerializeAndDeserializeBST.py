# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def preorder(node):
            if node:
                res.append(str(node.val))
                preorder(node.left)
                preorder(node.right)

        res = []
        preorder(root)
        return ' '.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        preorder = list(map(int, data.split(" ")))
        inorder = sorted(preorder)
        return self.formTree(preorder, inorder)

    def formTree(self, preorder, inorder):
        if inorder:
            root = TreeNode(preorder[0])
            inPos = inorder.index(preorder[0])
            preorder.pop(0)
            root.left = None if inPos == 0 else self.formTree(preorder, inorder[:inPos])
            root.right = None if inPos + 1 >= len(inorder) else self.formTree(preorder, inorder[inPos + 1:])
            return root

str = "-";
seq = ("a", "b", "c") # 字符串序列
print(str.join( seq ))
# join only works for string concatenation
str = "12364"
map(int,str)
# list(map(int,str)) = [1,2,3,6,4]
