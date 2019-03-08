"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: start: start value.
    @param: end: end value.
    @return: The root of Segment Tree.
    """
    def build(self, start, end):
        # 建到start == end那一层为止
        if start > end:
            return None
        root = SegmentTreeNode(start,end)
        # 注意start==end的时候不能继续递归，否则会无限循
        if start < end:
            root.left = self.build(start, (start + end) // 2)
            root.right = self.build((start + end) // 2 + 1, end)
        return root