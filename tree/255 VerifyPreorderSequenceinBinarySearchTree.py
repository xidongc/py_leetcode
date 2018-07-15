class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        if not preorder:
            return True
        stack = []
        low = -12345678
        for p in preorder:
            if p < low:
                return False
            while stack and p > stack[-1]:
                low = stack.pop()
            stack.append(p)
        return True

# False的条件为要么左子树出现了比右子树大的值，要么右子树的值比左子树小。两种情况都是右大于左的情况发生
#即正常为53267，非正常为52637，那么就需要让这个3被检测到
# 前序第一个必是root，然后是左子树，左子树加进去的时候没有val比root大的值。此时low应该就是root正常情况下，
# 因为 root是第一个被放进stack的val。后面如果有小于low的情况发生就是false
