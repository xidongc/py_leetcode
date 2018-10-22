from collections import namedtuple


class TreeNode(object):

    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class LinkedNode(object):

    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):

    def array_to_bst(self, arr):
        if len(arr) == 1:
            return TreeNode(arr[0])
        elif len(arr) < 1:
            return None
        mid = len(arr)//2
        root = TreeNode(arr[mid])
        root.left = self.array_to_bst(arr[0:mid])
        root.right = self.array_to_bst(arr[mid+1:])
        return root

    def ll_to_bst(self, head, end=None):
        if head == end:
            return None
        elif head.next == end:
            return TreeNode(head.val)

        slow = fast = head
        while fast is not end and fast.next is not end:
            fast = fast.next.next
            slow = slow.next
        root = TreeNode(slow.val)
        root.left = self.ll_to_bst(head, slow)
        root.right = self.ll_to_bst(slow.next, end)
        return root

    def in_order(self, root):
        if root is None:
            return
        self.in_order(root.left)
        print(root.val)
        self.in_order(root.right)

    @staticmethod
    def create_ll_from_arr(arr):
        head = LinkedNode(arr[0])
        curr = head
        for ele in arr[1:]:
            curr.next = LinkedNode(ele)
            curr = curr.next
        curr.next = None
        return head

    def print_ll(self, head):
        curr = head
        while curr is not None:
            print(curr.val)
            curr = curr.next

    def get_height(self, root):
        if root is None:
            return 0
        left = self.get_height(root.left)
        right = self.get_height(root.right)
        return max(left, right) + 1

    def morris_in_order_traversal(self, root):
        in_order = []
        curr = root
        while curr is not None:
            if curr.left is None:
                in_order.append(curr.val)
                curr = curr.right
            else:
                prev = curr.left
                while prev.right is not None and prev.right is not curr:
                    prev = prev.right
                if prev.right is None:
                    prev.right = curr
                    curr = curr.left
                elif prev.right is curr:
                    prev.right = None
                    in_order.append(curr.val)
                    curr = curr.right
        print(in_order)
        return in_order


s = Solution()
arr = [1,2,3,4,5,6,7,8,9]
#root = s.array_to_bst(arr)
#s.in_order(root)
head = s.create_ll_from_arr(arr)
root = s.ll_to_bst(head)
# s.in_order(root)
#s.print_ll(head)
#print(s.get_height(root))
s.morris_in_order_traversal(root)

