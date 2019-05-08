"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):

    def postorder(self, root):
        if not root:
            return list()
        stack1 = list()
        stack2 = list()
        output = list()

        stack1.append(root)
        while len(stack1):
            curr = stack1.pop()
            for c in curr.children:
                if c:
                    stack1.append(c)

            stack2.append(curr)
        while len(stack2):
            output.append(stack2.pop().val)

        return output
