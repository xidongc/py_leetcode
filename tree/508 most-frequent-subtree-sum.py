# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        map = {}
        maxTimes = 0
        def findTreeSum(root):
            if not root:
                return 0
            sum = root.val
            sum += findTreeSum(root.left)
            sum += findTreeSum(root.right)
            if sum in map:
                map[sum] += 1
            else:
                map[sum] = 1
            return sum
        findTreeSum(root)
        for key, value in map.items():
            if value > maxTimes:
                res = [key]
                maxTimes = value

            elif value == maxTimes:
                res.append(key)
        return res

root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(-3)

s = Solution()
s.findFrequentTreeSum(root)