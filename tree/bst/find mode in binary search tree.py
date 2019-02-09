class Solution(object):

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        global_val = list()
        global_num = 0

        if root is None:
            return global_val

        def in_traverse(root, result):
            if root is None:
                return
            in_traverse(root.left, result)
            result.append(root.val)
            in_traverse(root.right, result)
        result = list()
        in_traverse(root, result)

        pre_pointer = 0
        post_pointer = 1
        while post_pointer <= len(result) - 1:
            if result[post_pointer] == result[pre_pointer]:
                post_pointer += 1
            else:
                if post_pointer - pre_pointer > global_num:
                    global_val = [result[pre_pointer]]
                    global_num = post_pointer - pre_pointer
                elif post_pointer - pre_pointer == global_num:
                    global_val.append(result[pre_pointer])
                pre_pointer = post_pointer
                post_pointer += 1
        if post_pointer - pre_pointer > global_num:
            global_val = [result[pre_pointer]]
        elif post_pointer - pre_pointer == global_num:
            global_val.append(result[pre_pointer])

        return global_val