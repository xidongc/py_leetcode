# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        def helper(start, end):
            fast = slow = start
            if start == end:
                return None
            while fast is not end and fast.next is not end:
                slow = slow.next
                fast = fast.next.next
            node = TreeNode(slow.val)
            print(slow.val)
            node.left = helper(start, slow)
            node.right = helper(slow.next, end)
            return node

        return helper(head, None)

    # [-10,-3,0,5,9]
