"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None
"""


class Solution:
    """
    @param A: a list of integer
    @return: The root of Segment Tree
    """

    def build(self, A):
        # write your code here
        def helper(start, end):
            if start > end:
                return None
            root = SegmentTreeNode(start, end, max(A[start:end + 1]))
            if start < end:
                root.left = helper(start, (start + end) // 2)
                root.right = helper((start + end) // 2 + 1, end)
            return root

        return helper(0, len(A) - 1)

