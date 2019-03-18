# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import collections
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # BFS use queue
        if not root:
            return []
        res = collections.defaultdict(list)
        queue = [(root,0)]
        for node, pos in queue:

            if node:
                # print(node.val)
                res[pos].append(node.val)
                queue += (node.left, pos - 1), (node.right, pos + 1)
        #     sorted by keys
        return [res[i] for i in sorted(res)]

        # posMap = {}
        # def preTraversal(root, pos):
        #     if not root:
        #         return
        #     if pos not in posMap:
        #         posMap[pos] = [root.val]
        #     else:
        #         posMap[pos].append(root.val)
        #     preTraversal(root.left, pos - 1)
        #     preTraversal(root.right,pos + 1)
        # preTraversal(root,0)
        # od = collections.OrderedDict(sorted(posMap.items()))
        # return od.values()

# od = collections.OrderedDict(sorted(dict.items()))
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(8)
root.right.left = TreeNode(1)
root.right.right = TreeNode(7)
root.right.left.right = TreeNode(2)
s = Solution()
s.verticalOrder(root)
# import collections
#
# s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
#
# # defaultdict
# d = collections.defaultdict(list) default value is []
# d = collections.defaultdict(int) default value is 0
#
# for k, v in s:
#     print(k)
#     print(v)
#     # yellow
#     # 1
#     # blue
#     # 2
#     # yellow
#     # 3
#     # blue
#     # 4
#     # red
#     # 1
#     d[k].append(v)
# # dict_items([('yellow', [1, 3]), ('blue', [2, 4]), ('red', [1])])
#
# print(d.items())