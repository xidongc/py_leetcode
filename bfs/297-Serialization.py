# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec(object):

    def serialize(self, root):

        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        helper = []
        q = list()
        q.append(root)
        while len(q) > 0:
            curr = q.pop(0)
            if curr is None:
                helper.append("#")
            else:
                helper.append(curr.val)
                for i in [curr.left, curr.right]:
                    q.append(i)
        return " ".join(map(str, helper))

    def deserialize(self, data):
        data = data.split(" ")
        if data[0] is "#":
            return None
        root = TreeNode(int(data[0]))
        q = [root]
        start = 0
        while len(q) > 0 and start < len(data):
            curr = q.pop(0)
            if curr.left is None and start < len(data)-1:
                start += 1
                if data[start] is "#":
                    node = None
                else:
                    node = TreeNode(int(data[start]))
                    q.append(node)
                curr.left = node

            if curr.right is None and start < len(data)-1:
                start += 1
                if data[start] is "#":
                    node = None
                else:
                    node = TreeNode(int(data[start]))
                    q.append(node)
                curr.right = node
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))