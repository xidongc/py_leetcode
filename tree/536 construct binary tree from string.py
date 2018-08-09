# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
# Always emit the first '(' while traverse
# leaves sth like 2(3)(1) and 6(5))
#         s = "1234"
#         print(s[:-1]) "123"

        if not s or s == '(-)':
            return None
        pos = s.find('(')
        if pos == -1:
            return TreeNode(int(s))
        count = 0
        for j,ch in enumerate(s):
            if ch == '(': count += 1
            if ch == ')': count -= 1
            if count == 0 and j > pos:
                break
        cur = TreeNode(int(s[:pos]))
        cur.left = self.str2tree(s[pos + 1:j])
        cur.right = self.str2tree(s[j+2:-1])
        return cur

s = Solution()
s.str2tree("4(2(3)(1))(6(5))")
#                left  right

