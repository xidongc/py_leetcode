class Node(object):

    """  Segment tree node  """

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None


class NumArray(object):

    def __init__(self, nums):

        """
        :type nums: List[int]
        """

        def createTree(nums, l, r):
            if l > r:
                return None

            elif l == r:
                # leaf node
                n = Node(l, r)
                n.total = nums[l]
                return n

            mid = (l + r) // 2
            n = Node(l, r)
            n.left = createTree(nums, l, mid)
            n.right = createTree(nums, mid+1, r)
            n.total = n.left.total + n.right.total
            return n

        self.root = createTree(nums, 0, len(nums)-1)


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        def rangeSum(root, i, j):
            #If the range exactly matches the root, we already have the sum
            if root.start == i and root.end == j:
                return root.total

            mid = (root.start + root.end) // 2

            if i <= j <= mid:
                return rangeSum(root.left, i, j)
            elif j >= i > mid:
                return rangeSum(root.right, i, j)
            elif i < mid < j:
                return rangeSum(root.left, i, mid) + rangeSum(root.right, mid+1, j)

        return rangeSum(self.root, i, j)


